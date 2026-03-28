#!/usr/bin/env python3
"""
Validate a raw GPS L1 C/A navigation frame bitstream.

What this script does:
- Splits a bitstream into 30-bit NAV words
- Tries all 4 possible initial (previous D29*, previous D30*) states
  because the very first word depends on the last word before your frame
- De-inverts bits 1..24 of each word when previous D30* = 1
- Recomputes GPS parity for each word
- Reports parity pass/fail for every word
- Decodes basic subframe info from the HOW word:
    - TOW count (Z-count * 6 s)
    - subframe ID

Notes:
- Input can be one 1500-bit frame, or any multiple of 30 bits
- For a single isolated frame, the first word cannot be validated uniquely
  without knowing the previous word's D29*/D30*, so this script brute-forces it
- This is for GPS LNAV / L1 C/A 30-bit words

Reference convention:
- Each transmitted word is 30 bits:
    bits  1..24 = data bits (possibly inverted in transmission)
    bits 25..30 = parity bits
- "Previous D29*" and "previous D30*" are the transmitted bits 29 and 30
  of the previous word
"""

from dataclasses import dataclass
from typing import List, Tuple, Optional


@dataclass
class WordResult:
    word_index: int          # 0-based across whole stream
    subframe_index: int      # 0-based
    word_in_subframe: int    # 1..10
    raw_word: str            # transmitted 30 bits
    prev_d29: int
    prev_d30: int
    deinv_data: List[int]    # 24 de-inverted data bits
    rx_parity: List[int]     # received parity bits 25..30
    calc_parity: List[int]   # recomputed parity bits 25..30
    parity_ok: bool


@dataclass
class CandidateResult:
    initial_prev_d29: int
    initial_prev_d30: int
    words: List[WordResult]

    @property
    def ok_count(self) -> int:
        return sum(w.parity_ok for w in self.words)

    @property
    def total_count(self) -> int:
        return len(self.words)


def xor_bits(*args: int) -> int:
    x = 0
    for a in args:
        x ^= a
    return x


def bits_from_string(bitstr: str) -> List[int]:
    bitstr = "".join(c for c in bitstr if c in "01")
    if not bitstr:
        raise ValueError("No binary digits found.")
    return [int(c) for c in bitstr]


def split_words(bits: List[int], word_len: int = 30) -> List[List[int]]:
    if len(bits) % word_len != 0:
        raise ValueError(f"Bitstream length {len(bits)} is not a multiple of {word_len}.")
    return [bits[i:i + word_len] for i in range(0, len(bits), word_len)]


def de_invert_data_bits(raw_word: List[int], prev_d30: int) -> List[int]:
    """
    GPS LNAV words are transmitted with bits 1..24 inverted when previous D30* = 1.
    Parity bits 25..30 are not de-inverted here.
    """
    data = raw_word[:24]
    if prev_d30 == 1:
        return [b ^ 1 for b in data]
    return data[:]


def compute_lnav_parity(data24: List[int], prev_d29: int, prev_d30: int) -> List[int]:
    """
    Compute GPS LNAV parity bits D25..D30 from de-inverted data bits d1..d24
    and previous transmitted D29*, D30*.

    data24 is indexed 0..23 corresponding to d1..d24.
    """
    if len(data24) != 24:
        raise ValueError("data24 must contain 24 bits")

    d = [None] + data24  # 1-based indexing: d[1]..d[24]

    p25 = xor_bits(
        prev_d29, d[1], d[2], d[3], d[5], d[6], d[10], d[11], d[12], d[13], d[14],
        d[17], d[18], d[20], d[23]
    )
    p26 = xor_bits(
        prev_d30, d[2], d[3], d[4], d[6], d[7], d[11], d[12], d[13], d[14], d[15],
        d[18], d[19], d[21], d[24]
    )
    p27 = xor_bits(
        prev_d29, d[1], d[3], d[4], d[5], d[7], d[8], d[12], d[13], d[14], d[15],
        d[16], d[19], d[20], d[22]
    )
    p28 = xor_bits(
        prev_d30, d[2], d[4], d[5], d[6], d[8], d[9], d[13], d[14], d[15], d[16],
        d[17], d[20], d[21], d[23]
    )
    p29 = xor_bits(
        prev_d30, d[1], d[3], d[5], d[6], d[7], d[9], d[10], d[14], d[15], d[16],
        d[17], d[18], d[21], d[22], d[24]
    )
    p30 = xor_bits(
        prev_d29, d[3], d[5], d[6], d[8], d[9], d[10], d[11], d[13], d[15],
        d[19], d[22], d[23], d[24]
    )

    return [p25, p26, p27, p28, p29, p30]


def bits_to_uint(bits: List[int]) -> int:
    x = 0
    for b in bits:
        x = (x << 1) | b
    return x


def validate_candidate(words: List[List[int]], initial_prev_d29: int, initial_prev_d30: int) -> CandidateResult:
    prev_d29 = initial_prev_d29
    prev_d30 = initial_prev_d30
    results: List[WordResult] = []

    for wi, raw_word in enumerate(words):
        data24 = de_invert_data_bits(raw_word, prev_d30)
        rx_parity = raw_word[24:30]
        calc_parity = compute_lnav_parity(data24, prev_d29, prev_d30)
        parity_ok = (rx_parity == calc_parity)

        subframe_index = wi // 10
        word_in_subframe = (wi % 10) + 1

        results.append(
            WordResult(
                word_index=wi,
                subframe_index=subframe_index,
                word_in_subframe=word_in_subframe,
                raw_word="".join(str(b) for b in raw_word),
                prev_d29=prev_d29,
                prev_d30=prev_d30,
                deinv_data=data24,
                rx_parity=rx_parity,
                calc_parity=calc_parity,
                parity_ok=parity_ok,
            )
        )

        # Next word uses the transmitted D29*, D30* of this current word
        prev_d29 = raw_word[28]  # bit 29
        prev_d30 = raw_word[29]  # bit 30

    return CandidateResult(initial_prev_d29, initial_prev_d30, results)


def decode_tlm_preamble(word_result: WordResult) -> int:
    return bits_to_uint(word_result.deinv_data[:8])


def decode_how(word_result: WordResult) -> Tuple[int, int, int, int]:
    """
    HOW word fields from de-inverted data bits:
    bits 1..17  : Z-count
    bit 18      : alert
    bit 19      : anti-spoof
    bits 20..22 : subframe ID
    bits 23..24 : reserved

    Returns:
        z_count, tow_seconds, alert, subframe_id
    """
    d = word_result.deinv_data
    z_count = bits_to_uint(d[0:17])
    alert = d[17]
    antispoof = d[18]
    subframe_id = bits_to_uint(d[19:22])
    tow_seconds = z_count * 6
    return z_count, tow_seconds, alert, antispoof, subframe_id


def summarize_candidate(candidate: CandidateResult) -> None:
    print("=" * 80)
    print(
        f"Candidate initial previous bits: "
        f"D29*={candidate.initial_prev_d29}, D30*={candidate.initial_prev_d30}"
    )
    print(f"Parity passed: {candidate.ok_count}/{candidate.total_count}")

    if candidate.total_count % 10 != 0:
        print("Warning: stream is not an integer number of GPS subframes (10 words each).")

    n_subframes = candidate.total_count // 10
    print()

    for sf in range(n_subframes):
        tlm = candidate.words[sf * 10 + 0]
        how = candidate.words[sf * 10 + 1]

        preamble = decode_tlm_preamble(tlm)
        z_count, tow_seconds, alert, antispoof, subframe_id = decode_how(how)

        print(f"Subframe {sf + 1}:")
        print(f"  TLM preamble         : 0x{preamble:02X} ({preamble:08b})")
        print(f"  TLM parity ok        : {tlm.parity_ok}")
        print(f"  HOW parity ok        : {how.parity_ok}")
        print(f"  HOW Z-count          : {z_count}")
        print(f"  HOW TOW (seconds)    : {tow_seconds}")
        print(f"  HOW alert flag       : {alert}")
        print(f"  HOW anti-spoof flag  : {antispoof}")
        print(f"  HOW subframe ID      : {subframe_id}")
        print()

    print("Per-word parity:")
    for w in candidate.words:
        status = "OK" if w.parity_ok else "FAIL"
        print(
            f"  SF{w.subframe_index + 1} W{w.word_in_subframe:02d} : {status}  "
            f"prev(D29*,D30*)=({w.prev_d29},{w.prev_d30})  "
            f"rx={''.join(map(str, w.rx_parity))}  "
            f"calc={''.join(map(str, w.calc_parity))}"
        )
    print()


def choose_best_candidate(candidates: List[CandidateResult]) -> CandidateResult:
    return max(candidates, key=lambda c: c.ok_count)


def validate_bitstream(bitstr: str) -> List[CandidateResult]:
    bits = bits_from_string(bitstr)
    words = split_words(bits, 30)

    candidates = []
    for prev_d29 in (0, 1):
        for prev_d30 in (0, 1):
            candidates.append(validate_candidate(words, prev_d29, prev_d30))
    return candidates


if __name__ == "__main__":
    # Paste your bitstream here:
    BITSTREAM = "100010110000000000000010110111111111111111111001011000110011101000101001110111111111001111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111100010010111100100010010000000111000010110111111111110000000000011101101000001011010011101010001010010000100010110000000000000010110111111111111111110111010111101111011101100000010001110110010101110011010010100001101010001010001101110111010011101010000100111111000010110000000000010011010011110111101101001000100101111100101010010101011110010110000011010001001101111101011100000000011100001000000011000000100010110000000000000010110111111111111111110101010001100111000000000000110101011100110010100111110111100010110010110001000000000000001111011000101010000011000010010110000101001110001000000000110111111111010101111101101100101010000101111001000000000101100111000110000111011101100000010111111110101011011101001111111111111101001000000000000000001100110000100100010000010000000000000000111001111111111111111111111111010110000000000000000000000000101001111111111111111111111111010110000000000000000000000000101001111111111111111111111111010110000000000000000000000000101001111111111111111111111101110011011101001111111111111101001000000000000000001110110110101100010000010000000010110000101010000000100000101001011100010010111111111010011000000000001000101000010000110100010011001011010111000110000010000111000101000000001111011011001010111110100101010011011101110100001111110100100000000000011010111011"
    

    candidates = validate_bitstream(BITSTREAM)
    best = choose_best_candidate(candidates)

    print(f"Input bits: {len(bits_from_string(BITSTREAM))}")
    print(f"Words     : {len(bits_from_string(BITSTREAM)) // 30}")
    print()

    print("All candidate initial states:")
    for c in candidates:
        print(
            f"  initial prev(D29*,D30*)=({c.initial_prev_d29},{c.initial_prev_d30}) "
            f"-> {c.ok_count}/{c.total_count} words passed"
        )
    print()

    print("Best candidate:")
    summarize_candidate(best)