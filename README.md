# GPS Signal Simulator
> BSc Thesis — Python implementation

Generates a complete GPS L1 C/A signal including the LNAV navigation message and parity bits, constructed according to **IS-GPS-200N**. The output is validated against [GNSS-SDR](https://gnss-sdr.org/) and later GNU Radio to verify a position can be obtained from the synthetic signal.

## What it does

1. **NAV message generation** : Builds LNAV subframes 1–5 with correct bit layout (TLM, HOW, ephemeris, clock, almanac)
2. **Parity computation** : Applies the (32,26) Hamming code word-by-word, including D29*/D30* carry bits across word boundaries
3. **Signal generation** : BPSK modulates the C/A-code signal onto L1 and writes an IF sample file
4. **Validation** : Feeds the IF file into GNSS-SDR to confirm acquisition, tracking, and position output

## Planned: spoofing via signal delay

In a later stage, GNU Radio will be used to transmit the signal via SDR hardware. By introducing carefully controlled timing delays, the system will cause the receiver to calculate an incorrect (spoofed) location.

## Performance

Bit-level operations use the [`bitarray`](https://github.com/ilanschnell/bitarray) library for fast in-memory manipulation of the 1500-bit LNAV frames.

## Structure

Python functions which are complete, are saved in "functions.py" and may be imported into other documents to be used. Python functions which we are currently working on are saved in "to_gnss-sdr.ipynb".

## Reference

IS-GPS-200N — *NAVSTAR GPS Space Segment/Navigation User Segment Interfaces*