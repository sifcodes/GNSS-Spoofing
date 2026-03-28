from __future__ import annotations
from bitarray import bitarray
import numpy as np


def octal10_to_bits(o):
    # o is string like "0063"
    v = int(o, 8)              # octal → integer
    return [int(b) for b in f"{v:010b}"]  # → 10-bit list

octal10_to_bits("0775")


CA_PRN_1_37 = {


    # Select by Space Vehicle number and first 10 octal for sanity check
    "SV_select": {
        1:  ((2, 6), "1440"),
        2:  ((3, 7), "1620"),
        3:  ((4, 8), "1710"),
        4:  ((5, 9), "1744"),
        5:  ((1, 9), "1133"),
        6:  ((2,10), "1455"),
        7:  ((1, 8), "1131"),
        8:  ((2, 9), "1454"),
        9:  ((3,10), "1626"),
        10: ((2, 3), "1504"),
        11: ((3, 4), "1642"),
        12: ((5, 6), "1750"),
        13: ((6, 7), "1764"),
        14: ((7, 8), "1772"),
        15: ((8, 9), "1775"),
        16: ((9,10), "1776"),
        17: ((1, 4), "1156"),
        18: ((2, 5), "1467"),
        19: ((3, 6), "1633"),
        20: ((4, 7), "1715"),
        21: ((5, 8), "1746"),
        22: ((6, 9), "1763"),
        23: ((1, 3), "1063"),
        24: ((4, 6), "1706"),
        25: ((5, 7), "1743"),
        26: ((6, 8), "1761"),
        27: ((7, 9), "1770"),
        28: ((8,10), "1774"),
        29: ((1, 6), "1127"),
        30: ((2, 7), "1453"),
        31: ((3, 8), "1625"),
        32: ((4, 9), "1712"),
        65: ((5,10), "1745"),
        66: ((4,10), "1713"),
        67: ((1, 7), "1134"),
        68: ((2, 8), "1456"),
        69: ((4,10), "1713"),  # identical C/A to PRN 34
    },


    # Select by PRN number and first 10 octal for sanity check
    "phase_select": {
        1:  ((2, 6), "1440"),
        2:  ((3, 7), "1620"),
        3:  ((4, 8), "1710"),
        4:  ((5, 9), "1744"),
        5:  ((1, 9), "1133"),
        6:  ((2,10), "1455"),
        7:  ((1, 8), "1131"),
        8:  ((2, 9), "1454"),
        9:  ((3,10), "1626"),
        10: ((2, 3), "1504"),
        11: ((3, 4), "1642"),
        12: ((5, 6), "1750"),
        13: ((6, 7), "1764"),
        14: ((7, 8), "1772"),
        15: ((8, 9), "1775"),
        16: ((9,10), "1776"),
        17: ((1, 4), "1156"),
        18: ((2, 5), "1467"),
        19: ((3, 6), "1633"),
        20: ((4, 7), "1715"),
        21: ((5, 8), "1746"),
        22: ((6, 9), "1763"),
        23: ((1, 3), "1063"),
        24: ((4, 6), "1706"),
        25: ((5, 7), "1743"),
        26: ((6, 8), "1761"),
        27: ((7, 9), "1770"),
        28: ((8,10), "1774"),
        29: ((1, 6), "1127"),
        30: ((2, 7), "1453"),
        31: ((3, 8), "1625"),
        32: ((4, 9), "1712"),
        33: ((5,10), "1745"),
        34: ((4,10), "1713"),
        35: ((1, 7), "1134"),
        36: ((2, 8), "1456"),
        37: ((4,10), "1713"),
    },
}


CA_PRN_1_37["phase_select"].get(1)[1]


CA_PRN_38_63 = {


    # Select by Space Vehicle ID number (GPS III/IIIF blocks)
    # value = (G2_delay_chips, initial_G2_setting_octal, first_10_chips_octal)
    "SV_select": {
        70: (  67, "0017", "1760"),
        71: ( 103, "0541", "1236"),
        72: (  91, "1714", "0063"),
        73: (  19, "1151", "0626"),
        74: ( 679, "1651", "0126"),
        75: ( 225, "0103", "1674"),
        76: ( 625, "0543", "1234"),
        77: ( 946, "1506", "0271"),
        78: ( 638, "1065", "0712"),
        79: ( 161, "1564", "0213"),
        80: (1001, "1365", "0412"),
        81: ( 554, "1541", "0236"),
        82: ( 280, "1327", "0450"),
        83: ( 710, "1716", "0061"),
        84: ( 709, "1635", "0142"),
        85: ( 775, "1002", "0775"),
        86: ( 864, "1015", "0762"),
        87: ( 558, "1666", "0111"),
        88: ( 220, "0177", "1600"),
        89: ( 397, "1353", "0424"),
        90: (  55, "0426", "1351"),
        91: ( 898, "0227", "1550"),
        92: ( 759, "0506", "1271"),
        93: ( 367, "0336", "1441"),
        94: ( 299, "1333", "0444"),
        95: (1018, "1745", "0032"),
    },


    # Select by PRN number (38–63)
    # value = (G2_delay_chips, initial_G2_setting_octal, first_10_chips_octal)
    "shift_select": {
        38: (  67, "0017", "1760"),
        39: ( 103, "0541", "1236"),
        40: (  91, "1714", "0063"),
        41: (  19, "1151", "0626"),
        42: ( 679, "1651", "0126"),
        43: ( 225, "0103", "1674"),
        44: ( 625, "0543", "1234"),
        45: ( 946, "1506", "0271"),
        46: ( 638, "1065", "0712"),
        47: ( 161, "1564", "0213"),
        48: (1001, "1365", "0412"),
        49: ( 554, "1541", "0236"),
        50: ( 280, "1327", "0450"),
        51: ( 710, "1716", "0061"),
        52: ( 709, "1635", "0142"),
        53: ( 775, "1002", "0775"),
        54: ( 864, "1015", "0762"),
        55: ( 558, "1666", "0111"),
        56: ( 220, "0177", "1600"),
        57: ( 397, "1353", "0424"),
        58: (  55, "0426", "1351"),
        59: ( 898, "0227", "1550"),
        60: ( 759, "0506", "1271"),
        61: ( 367, "0336", "1441"),
        62: ( 299, "1333", "0444"),
        63: (1018, "1745", "0032"),
    },
}


# Example access (like your PRN 1–37 dict):
CA_PRN_38_63["shift_select"].get(40)[1]   # -> G2 delay chips for PRN 38




def ca_code(PRN):
    """ Tager PRN-nummer som input og giver C/A-kode som output"""

    # Metode 1: Fra PRN 0-37

    # Definer G2 (ændrer sig ikke)
    G2 = [2, 3, 6, 8, 9, 10] 

    cacode= []
    
    if PRN <= 37:
        reg1 = []+10*[1]                          # Definer initial register (liste med 10 1'ere)
        reg2 = []+10*[1]                          # Definer initial register (liste med 10 1'ere)

        # Definer G1
        G1 = CA_PRN_1_37["phase_select"][PRN][0]  # Liste med kun [2, 6]

        for i in range(1023):

            # Tjek om der er 0 eller 1 på pladserne i G1 og G2, læg dem sammen. Lige = 0, ulige = 1
            reg1temp = reg1[G1[1-1]-1] ^  reg1[G1[2-1]-1]
            reg2temp = (reg2[G2[1-1]-1] ^  reg2[G2[2-1]-1]  ^  reg2[G2[3-1]-1] ^  
                       reg2[G2[4-1]-1]  ^  reg2[G2[5-1]-1] ^  reg2[G2[6-1]-1])
            
            # Sammenlign sidste entry i reg1 med G1 og append til C/A-kode
            cacode.append((reg1[-1]  ^  reg2[G1[1-1]-1] ^  reg2[G1[2-1]-1]))

            # Opdater registre med shift
            reg1 = [reg1temp]+reg1[:-1] 
            reg2 = [reg2temp] + reg2[:-1]

        #print("Valid:", cacode[:10] == octal10_to_bits(CA_PRN_1_37["phase_select"].get(PRN)[1]))
        return bitarray(cacode)

    # Metode 2: Fra PRN 38-63 not relevant as we only look at L1 band 1-32 sats
    else:               
        reg1 = []+10*[1]

        # Modificeret reg2 ift. initial conditions
        reg2 = octal10_to_bits(CA_PRN_38_63["shift_select"].get(PRN)[1])
        reg2.reverse()

        # Definer G1
        G1 = [3, 10]                            # Ændres ikke            

        for i in range(1023):

            # Tjek om der er 0 eller 1 på pladserne i G1 og G2, læg dem sammen. Lige = 0, ulige = 1
            reg1temp = reg1[G1[1-1]-1] ^  reg1[G1[2-1]-1]
            reg2temp = (reg2[G2[1-1]-1] ^  reg2[G2[2-1]-1]  ^  reg2[G2[3-1]-1] ^ 
                        reg2[G2[4-1]-1]  ^  reg2[G2[5-1]-1] ^  reg2[G2[6-1]-1])

            # Sammenlign sidste value i hvert register og appender til C/A-kode
            cacode.append((reg1[-1]  ^  reg2[-1]))

            # Opdater registre med shift
            reg1 = [reg1temp]+reg1[:-1]
            reg2 = [reg2temp] + reg2[:-1]

        print("Valid:" , cacode[:10] == octal10_to_bits(CA_PRN_38_63["shift_select"].get(PRN)[2]))
        return bitarray(cacode)



ca_code(20)

def compute_parity(word_current, D29, D30):
    data24 = word_current.copy()     #laziness, changing data24 would take ages
    # now compute parity


    p1 = D29 ^ data24[0] ^ data24[1] ^ data24[2] ^ data24[4] ^ data24[5] ^ data24[9] ^ data24[10] ^ data24[11] ^ data24[12] ^ data24[13] ^ data24[16] ^ data24[17] ^ data24[19] ^ data24[22]
    p2 = D30 ^ data24[1] ^ data24[2] ^ data24[3] ^ data24[5] ^ data24[6] ^ data24[10] ^ data24[11] ^ data24[12] ^ data24[13] ^ data24[14] ^ data24[17] ^ data24[18] ^ data24[20] ^ data24[23]
    p3 = D29 ^ data24[0] ^ data24[2] ^ data24[3] ^ data24[4] ^ data24[6] ^ data24[7] ^ data24[11] ^ data24[12] ^ data24[13] ^ data24[14] ^ data24[15] ^ data24[18] ^ data24[19] ^ data24[21]
    p4 = D30 ^ data24[1] ^ data24[3] ^ data24[4] ^ data24[5] ^ data24[7] ^ data24[8] ^ data24[12] ^ data24[13] ^ data24[14] ^ data24[15] ^ data24[16] ^ data24[19] ^ data24[20] ^ data24[22]
    p5 = D30 ^ data24[0] ^ data24[2] ^ data24[4] ^ data24[5] ^ data24[6] ^ data24[8] ^ data24[9] ^ data24[13] ^ data24[14] ^ data24[15] ^ data24[16] ^ data24[17] ^ data24[20] ^ data24[21] ^ data24[23]
    p6 = D29 ^ data24[2] ^ data24[4] ^ data24[5] ^ data24[7] ^ data24[8] ^ data24[9] ^ data24[10] ^ data24[12] ^ data24[14] ^ data24[18] ^ data24[21] ^ data24[22] ^ data24[23]

    if D30 == 1:                                  
        data24.invert()
    parity = bitarray([p1, p2, p3, p4, p5, p6])
    
    data30 = bitarray(0)
    data30 += data24 + parity
    return data30


def solve_word_2_10_bits(word24, D29_star, D30_star):
    w = word24.copy()

    if len(w) < 24:
        w.extend([0] * (24 - len(w)))
    elif len(w) > 24:
        raise ValueError(f"word must be 24 bits before parity, got {len(w)}")

    # Force p5 = 0 using your compute_parity convention
    w[23] = (
        w[0] ^ w[2] ^ w[4] ^ w[5] ^ w[6] ^ w[8] ^ w[9] ^
        w[13] ^ w[14] ^ w[15] ^ w[16] ^ w[17] ^ w[20] ^ w[21]
    )

    # Force p6 = 0 using your compute_parity convention
    w[22] = (
        D29_star ^ D30_star ^
        w[2] ^ w[4] ^ w[5] ^ w[7] ^ w[8] ^ w[9] ^ w[10] ^
        w[12] ^ w[14] ^ w[18] ^ w[21] ^ w[23]
    )

    return w


def append_parity(list10wrd5sub25frame):
    """Takes the previous word and the current word as input
    to compute the parity for the current word. Return the 6-bit parity"""

    Z_count=list10wrd5sub25frame[1]
    list10wrd5sub25frame=list10wrd5sub25frame[0]
    message = bitarray(0)
    for k in range(25):
        for j in range(5):
            for i in range(10):
                if i == 0 and j == 0 and k == 0:
                    D29 = 0
                    D30 = 0
                    message.extend(compute_parity(list10wrd5sub25frame[k][j][0][i],D29,D30)) #data append

                elif i in (1,9):    
                    D29,D30 = message[-2], message[-1]               
                    list10wrd5sub25frame[k][j][0][i] = solve_word_2_10_bits(list10wrd5sub25frame[k][j][0][i], D29, D30)
                    message.extend(compute_parity(list10wrd5sub25frame[k][j][0][i],D29,D30)) #data append
                else:
                    D29,D30 = message[-2], message[-1]
                    message.extend(compute_parity(list10wrd5sub25frame[k][j][0][i],D29,D30)) #data append   


    return message, Z_count



"""
GPS LNAV (IS-GPS-200) ephemeris re-encoding helpers:
Convert RINEX-style values (typically floats; angles/rates in radians) into:
  1) the transmitted integer field value (N)
  2) the fixed-width bitstring (two's complement if signed)

Covers the common Subframe 1 (clock), Subframe 2/3 (orbit) fields:
  sqrtA, e, M0, Omega0, omega, i0, DeltaN, Cuc/Cus/Cic/Cis, Crc/Crs, Toe, OmegaDot, IDOT
"""

import math
from dataclasses import dataclass
from typing import Tuple, Dict, Any
import pandas as pd

# ---------------------------
# Core helpers
# ---------------------------

def rad_to_semicircles(x_rad: float) -> float:
    """Convert radians -> semi-circles (GPS ICD uses semi-circles for angles)."""
    return x_rad / math.pi


def radps_to_semicirclesps(x_rad_per_s: float) -> float:
    """Convert rad/s -> semi-circles/s."""
    return x_rad_per_s / math.pi


def encode_unsigned(value: float, lsb: float, bits: int) -> int:
    """Quantize to an unsigned integer field with given LSB and bit-width."""
    n = int(round(value / lsb))
    if n < 0 or n >= (1 << bits):
        raise ValueError(f"Unsigned overflow: n={n} not in [0, {2**bits - 1}]")
    return n


def encode_signed(value: float, lsb: float, bits: int) -> int:
    """Quantize to a signed integer field (two's complement) with given LSB and bit-width."""
    n = int(round(value / lsb))
    min_n = -(1 << (bits - 1))
    max_n = (1 << (bits - 1)) - 1
    if n < min_n or n > max_n:
        raise ValueError(f"Signed overflow: n={n} not in [{min_n}, {max_n}]")
    return n


def int_to_bits(n: int, bits: int) -> str:
    """
    Convert integer to fixed-width bitstring.
    Works for signed or unsigned if 'n' is the signed integer:
      - For negative, wraps by masking to bits (two's complement).
    """
    return format(n & ((1 << bits) - 1), f"0{bits}b")


def encode_field_unsigned(value: float, lsb: float, bits: int) -> Tuple[int, str]:
    n = encode_unsigned(value, lsb, bits)
    return n, int_to_bits(n, bits)


def encode_field_signed(value: float, lsb: float, bits: int) -> Tuple[int, str]:
    n = encode_signed(value, lsb, bits)
    return n, int_to_bits(n, bits)


# ---------------------------
# GPS LNAV parameter encoders
# (RINEX -> LNAV field int + bits)
# ---------------------------

# ---- Subframe 2/3: Orbit ----

def enc_sqrtA(sqrtA_sqrtm: float) -> Tuple[int, str]:
    # 32 bits unsigned, LSB 2^-19 sqrt(m)
    return encode_field_unsigned(sqrtA_sqrtm, 2**-19, 32)


def enc_e(e: float) -> Tuple[int, str]:
    # 32 bits unsigned, LSB 2^-33
    return encode_field_unsigned(e, 2**-33, 32)


def enc_M0(M0_rad: float) -> Tuple[int, str]:
    # 32 bits signed, LSB 2^-31 semi-circles
    x_sc = rad_to_semicircles(M0_rad)
    return encode_field_signed(x_sc, 2**-31, 32)


def enc_Omega0(Omega0_rad: float) -> Tuple[int, str]:
    # 32 bits signed, LSB 2^-31 semi-circles
    x_sc = rad_to_semicircles(Omega0_rad)
    return encode_field_signed(x_sc, 2**-31, 32)


def enc_omega(omega_rad: float) -> Tuple[int, str]:
    # 32 bits signed, LSB 2^-31 semi-circles
    x_sc = rad_to_semicircles(omega_rad)
    return encode_field_signed(x_sc, 2**-31, 32)


def enc_i0(i0_rad: float) -> Tuple[int, str]:
    # 32 bits signed, LSB 2^-31 semi-circles
    x_sc = rad_to_semicircles(i0_rad)
    return encode_field_signed(x_sc, 2**-31, 32)


def enc_DeltaN(DeltaN_rad_per_s: float) -> Tuple[int, str]:
    # 16 bits signed, LSB 2^-43 semi-circles/s
    x_scps = radps_to_semicirclesps(DeltaN_rad_per_s)
    return encode_field_signed(x_scps, 2**-43, 16)


def enc_Cuc(Cuc_rad: float) -> Tuple[int, str]:
    # 16 bits signed, LSB 2^-29 radians
    return encode_field_signed(Cuc_rad, 2**-29, 16)


def enc_Cus(Cus_rad: float) -> Tuple[int, str]:
    # 16 bits signed, LSB 2^-29 radians
    return encode_field_signed(Cus_rad, 2**-29, 16)


def enc_Cic(Cic_rad: float) -> Tuple[int, str]:
    # 16 bits signed, LSB 2^-29 radians
    return encode_field_signed(Cic_rad, 2**-29, 16)


def enc_Cis(Cis_rad: float) -> Tuple[int, str]:
    # 16 bits signed, LSB 2^-29 radians
    return encode_field_signed(Cis_rad, 2**-29, 16)


def enc_Crc(Crc_m: float) -> Tuple[int, str]:
    # 16 bits signed, LSB 2^-5 meters
    return encode_field_signed(Crc_m, 2**-5, 16)


def enc_Crs(Crs_m: float) -> Tuple[int, str]:
    # 16 bits signed, LSB 2^-5 meters
    return encode_field_signed(Crs_m, 2**-5, 16)


def enc_Toe(Toe_s: float) -> Tuple[int, str]:
    # 16 bits unsigned, LSB 16 seconds (2^4)
    return encode_field_unsigned(Toe_s, 16.0, 16)


def enc_OmegaDot(OmegaDot_rad_per_s: float) -> Tuple[int, str]:
    # 24 bits signed, LSB 2^-43 semi-circles/s
    x_scps = radps_to_semicirclesps(OmegaDot_rad_per_s)
    return encode_field_signed(x_scps, 2**-43, 24)


def enc_IDOT(IDOT_rad_per_s: float) -> Tuple[int, str]:
    # 14 bits signed, LSB 2^-43 semi-circles/s
    x_scps = radps_to_semicirclesps(IDOT_rad_per_s)
    return encode_field_signed(x_scps, 2**-43, 14)


# ---- Subframe 1: Clock ----

def enc_af0(af0_s: float) -> Tuple[int, str]:
    # 22 bits signed, LSB 2^-31 seconds
    return encode_field_signed(af0_s, 2**-31, 22)


def enc_af1(af1_s_per_s: float) -> Tuple[int, str]:
    # 16 bits signed, LSB 2^-43 s/s
    return encode_field_signed(af1_s_per_s, 2**-43, 16)


def enc_af2(af2_s_per_s2: float) -> Tuple[int, str]:
    # 8 bits signed, LSB 2^-55 s/s^2
    return encode_field_signed(af2_s_per_s2, 2**-55, 8)





# Subframe one TGD
def enc_TGD(TGD: float) -> Tuple[int, str]:
    # 8 bits signed, LSB^-31 s
    return encode_field_signed(TGD,2**-31,8)


#FitIntvl
def enc_FitIntvl(FitIntvl: float) -> Tuple[int,str]:
    #4 mean 0, above 4 means 1
    if FitIntvl <= 4:
        bit = 0
    else:
        bit = 1
    return int(FitIntvl),format(bit,"01b")


#IODE
def enc_IODE(IODE: float) -> Tuple[int, str]:
    # 8 bits unsigned, LSB 1 issue number
    return encode_field_unsigned(IODE,1,8)


#IODC
def enc_IODC(IODC: float) -> Tuple[int, str]:
    # 10 bits unsigned, LSB 1 issue number
    return encode_field_unsigned(IODC,1,10)


#Toc
def enc_Toc(Toc: float) -> Tuple[int, str]:
    # 16 bits unsigned, LSB 2^4 seconds
    return encode_field_unsigned(datetime_to_gpsweek_and_sow(Toc)[1],2**4,16)

def datetime_to_gpsweek_and_sow(dt):
    gps0 = pd.Timestamp("1980-01-06T00:00:00Z")
    dt = pd.Timestamp(dt)
    dt = dt.tz_localize("UTC") if dt.tzinfo is None else dt.tz_convert("UTC")
    sec = (dt - gps0).total_seconds()
    week = int(sec // 604800)
    sow = round(sec - week * 604800)
    return week, sow

#GPSWeek
def enc_GPSWeek(GPSWeek: float) -> Tuple[int, str]:
    # 10 bits unsigned, LSB 1 
    week=int(round(GPSWeek))
    wn10=week%1014 #rollover correction
    return encode_field_unsigned(wn10,1,10)


#URAIdx
def enc_URAIdx(URAIdx: float) -> Tuple[int, str]:
    # 4 bits unsigned, LSB 1 seconds
    return encode_field_unsigned(URAIdx,1,4)


#TOW
def enc_TOW(TOW: float) -> Tuple[int, str]:
    # 17 bits unsigned, LSB 6 seconds
    if TOW > 604800:
        TOW=0
    return encode_field_unsigned(TOW,6,17)


#deltai
def enc_deltai(Io: float) -> Tuple[int, str]:
    #16 bits signed, LSB 2^-19 semi circles
    deltai=rad_to_semicircles(Io)-0.3
    return encode_field_signed(deltai,2**-19,16)


#TOA
def enc_TOA(TOE: float) -> Tuple[int, str]:
    #8 bits unsigned, LSB 2^12 seconds
    return encode_field_unsigned(TOE,2**12,8)


#alpha0
def enc_alpha0(alpha0: float) -> Tuple[int, str]:
    #8 bits signed, LSB 2^-30 seconds
    return encode_field_signed(alpha0,2**-30,8)

#alpha1
def enc_alpha1(alpha1: float) -> Tuple[int, str]:
    #8 bits signed, LSB 2^-27 seconds
    return encode_field_signed(alpha1,2**-27,8)

#alpha2
def enc_alpha2(alpha2: float) -> Tuple[int, str]:
    #8 bits signed, LSB 2^-24 seconds
    return encode_field_signed(alpha2,2**-24,8)

#alpha3
def enc_alpha3(alpha3: float) -> Tuple[int, str]:
    #8 bits signed, LSB 2^-24 seconds
    return encode_field_signed(alpha3,2**-24,8)

#beta0
def enc_beta0(beta0: float) -> Tuple[int, str]:
    #8 bits signed, LSB 2^11 seconds
    return encode_field_signed(beta0,2**11,8)

#beta1
def enc_beta1(beta1: float) -> Tuple[int, str]:
    #8 bits signed, LSB 2^14 seconds
    return encode_field_signed(beta1,2**14,8)

#beta2
def enc_beta2(beta2: float) -> Tuple[int, str]:
    #8 bits signed, LSB 2^16 seconds
    return encode_field_signed(beta2,2**16,8)

#beta3
def enc_beta3(beta3: float) -> Tuple[int, str]:
    #8 bits signed, LSB 2^16 seconds
    return encode_field_signed(beta3,2**16,8)


# --- UTC Time Parameters (Subframe 4 Page 18) ---

def enc_A1(A1: float):
    # 24 bits signed, LSB 2^-50 s/s
    return encode_field_signed(A1, 2**-50, 24)

def enc_A0(A0: float):
    # 32 bits signed, LSB 2^-30 s
    return encode_field_signed(A0, 2**-30, 32)

def enc_tot(tot: float):
    # 8 bits unsigned, LSB 2^12 seconds
    return encode_field_unsigned(tot, 2**12, 8)

def enc_WNt(WNt: int):
    # 8 bits unsigned, LSB 1 week
    WNt = WNt% 256
    return encode_field_unsigned(WNt, 1, 8)

def enc_dtLS(dtLS: int):
    # 8 bits signed, LSB 1 second
    return encode_field_signed(dtLS, 1, 8)

def enc_WNLSF(WNLSF: int):
    # 8 bits unsigned, LSB 1 week
    return encode_field_unsigned(WNLSF, 1, 8)

def enc_DN(DN: int):
    # 8 bits unsigned, LSB 1 day
    return encode_field_unsigned(DN, 1, 8)

def enc_dtLSF(dtLSF: int):
    # 8 bits signed, LSB 1 second
    return encode_field_signed(dtLSF, 1, 8)


#WNa
def enc_WNa(GPSWeek: int):
    # 8 bits unsigned, LSB 1 week
    WNa = GPSWeek% 256
    return encode_field_unsigned(WNa, 1, 8)



# ---------------------------
# Convenience: encode a whole "row"
# ---------------------------

@dataclass
class EncodedField:
    n: int
    bits: str

def encode_gps_lnav_ephemeris(params: Dict[str, Any]) -> Dict[str, EncodedField]:
    """
    Encode a dict of RINEX-like values for one SV/epoch into LNAV field ints + bitstrings.
    Required keys (orbit):
      sqrtA, e, i0, Omega0, omega, M0, Toe, DeltaN, Cuc, Cus, Crc, Crs, Cic, Cis, OmegaDot, IDOT
    Optional keys (clock):
      af0, af1, af2
    """
    out: Dict[str, EncodedField] = {}

    # Orbit (subframes 2/3)
    out["sqrtA"]    = EncodedField(*enc_sqrtA(params["sqrtA"]))
    out["Eccentricity"]        = EncodedField(*enc_e(params["e"]))
    out["Io"]       = EncodedField(*enc_i0(params["i0"]))
    out["Omega0"]   = EncodedField(*enc_Omega0(params["Omega0"]))
    out["omega"]    = EncodedField(*enc_omega(params["omega"]))
    out["M0"]       = EncodedField(*enc_M0(params["M0"]))
    out["Toe"]      = EncodedField(*enc_Toe(params["Toe"]))
    out["DeltaN"]   = EncodedField(*enc_DeltaN(params["DeltaN"]))
    out["Cuc"]      = EncodedField(*enc_Cuc(params["Cuc"]))
    out["Cus"]      = EncodedField(*enc_Cus(params["Cus"]))
    out["Crc"]      = EncodedField(*enc_Crc(params["Crc"]))
    out["Crs"]      = EncodedField(*enc_Crs(params["Crs"]))
    out["Cic"]      = EncodedField(*enc_Cic(params["Cic"]))
    out["Cis"]      = EncodedField(*enc_Cis(params["Cis"]))
    out["OmegaDot"] = EncodedField(*enc_OmegaDot(params["OmegaDot"]))
    out["IDOT"]     = EncodedField(*enc_IDOT(params["IDOT"]))
    out["TGD"]      = EncodedField(*enc_TGD(params["TGD"]))
    out["FitIntvl"] = EncodedField(*enc_FitIntvl(params["FitIntvl"]))
    out["IODE"]     = EncodedField(*enc_IODE(params["IODE"]))
    out["Toc"]      = EncodedField(*enc_Toc(params["time"]))
    out["GPSWeek"]  = EncodedField(*enc_GPSWeek(params["GPSWeek"]))
    out["IODC"]     = EncodedField(*enc_IODC(params["IODC"]))
    out["URAIdx"]   = EncodedField(*enc_URAIdx(params["URAIdx"]))
    out["TOW"]      = EncodedField(*enc_TOW(params["TOW"]))
    out["deltai"]   = EncodedField(*enc_deltai(params["deltai"]))
    out["TOA"]      = EncodedField(*enc_TOA(params["TOA"]))
    out["alpha0"]   = EncodedField(*enc_alpha0(params["alpha0"]))
    out["alpha1"]   = EncodedField(*enc_alpha1(params["alpha1"]))
    out["alpha2"]   = EncodedField(*enc_alpha2(params["alpha2"]))
    out["alpha3"]   = EncodedField(*enc_alpha3(params["alpha3"]))
    out["beta0"]    = EncodedField(*enc_beta0(params["beta0"]))
    out["beta1"]    = EncodedField(*enc_beta1(params["beta1"]))
    out["beta2"]    = EncodedField(*enc_beta2(params["beta2"]))
    out["beta3"]    = EncodedField(*enc_beta3(params["beta3"]))
    out["A0"]       = EncodedField(*enc_A0(params["A0"]))
    out["A1"]       = EncodedField(*enc_A1(params["A1"]))
    out["tot"]      = EncodedField(*enc_tot(params["tot"]))
    out["WNt"]      = EncodedField(*enc_WNt(params["WNt"]))
    out["dtLS"]     = EncodedField(*enc_dtLS(params["dtLS"]))
    out["dtLSF"]    = EncodedField(*enc_dtLSF(params["dtLSF"]))
    out["WNLSF"]    = EncodedField(*enc_WNLSF(params["WNLSF"]))
    out["DN"]       = EncodedField(*enc_DN(params["DN"]))
    out["WNa"]      = EncodedField(*enc_WNa(params["WNa"]))

    # Clock (subframe 1) if provided
    if "af0" in params:
        out["af0"] = EncodedField(*enc_af0(params["af0"]))
    if "af1" in params:
        out["af1"] = EncodedField(*enc_af1(params["af1"]))
    if "af2" in params:
        out["af2"] = EncodedField(*enc_af2(params["af2"]))

    return out



#code field ONLY needed because georinex doesnt show general time corrections....
import re
from pathlib import Path

# matches numbers like: -1.23E-09, 233472, -2.220446049E-15
NUM_RE = re.compile(r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[Ee][+-]?\d+)?')  #this gibberish is a search pattern that extracts sci numbers, needed because numbers like this -1.2805685401E-09-2.220446049E-15 are without space between them in rinex 3.x

def parse_rinex_utc_params(rnx_path: str):
    """
    Extract GPS->UTC (GPUT) and leap seconds from a RINEX 3 NAV header.
    If leap-second scheduling fields are missing, fill for simulation with:
      dtLSF = dtLS, WNLSF = 0, DN = 0
    Returns: dict(A0, A1, tot, WNt, dtLS, dtLSF, WNLSF, DN)
    """
    A0 = A1 = tot = WNt = None
    dtLS = dtLSF = WNLSF = DN = None

    with Path(rnx_path).open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            label = line[60:80].strip()

            if label == "END OF HEADER":
                break

            if label == "TIME SYSTEM CORR":
                corr_id = line[:4].strip()
                if corr_id == "GPUT":
                    nums = NUM_RE.findall(line[:60])
                    if len(nums) >= 4:
                        A0 = float(nums[0])
                        A1 = float(nums[1])
                        tot = int(float(nums[2]))
                        WNt = int(float(nums[3]))

            if label == "LEAP SECONDS":
                nums = NUM_RE.findall(line[:60])
                if len(nums) >= 1: dtLS  = int(float(nums[0]))
                if len(nums) >= 2: dtLSF = int(float(nums[1]))
                if len(nums) >= 3: WNLSF = int(float(nums[2]))
                if len(nums) >= 4: DN    = int(float(nums[3]))

    # Simulation-friendly defaults if missing
    if dtLS is not None:
        if dtLSF is None:
            dtLSF = dtLS
        if WNLSF is None:
            WNLSF = 0
        if DN is None:
            DN = 0

    return {
        "A0": A0, "A1": A1, "tot": tot, "WNt": WNt,
        "dtLS": dtLS, "dtLSF": dtLSF, "WNLSF": WNLSF, "DN": DN
    }


path = "BUDD00DNK_R_20260110000_01D_MN.rnx"
utc = parse_rinex_utc_params(path)
# should give approximately:
# {'A0': 1.8626451492e-09, 'A1': 5.329070518e-15, 'tot': 233472, 'WNt': 2401, 'dtLS': 18}


import georinex as gr
import warnings

warnings.simplefilter("ignore", FutureWarning)

nav = gr.load("BUDD00DNK_R_20260110000_01D_MN.rnx",use="G")   # can also be .rnx.gz in many cases
#print(nav)  

# list GPS satellites present
gps_svs = [sv for sv in nav.sv.values if str(sv).startswith("G")]
#print("GPS SVs:", gps_svs[:10], "... total:", len(gps_svs))

tables = {}
# pick one SV at a time
for i in gps_svs:
    sv = i
    eph = nav.sel(sv=sv)
    nav.sel(sv=sv)["time"].values
    # show key orbital params if present
    keys = ['SVclockBias', 'SVclockDrift', 'SVclockDriftRate', 'IODE', 'Crs', 'DeltaN', 'M0', 'Cuc', 'Eccentricity', 'Cus', 'sqrtA', 'Toe', 'Cic', 'Omega0', 'Cis', 'Io', 'Crc', 'omega', 'OmegaDot', 'IDOT', 'GPSWeek', 'SVacc', 'health', 'TGD', 'IODC', 'TransTime',"GPSWeek","FitIntvl","time"]
    #keys = [k for k in keys if k in eph.data_vars]
    df = eph[keys].to_dataframe()

    iono = nav.attrs["ionospheric_corr_GPS"]
    alpha0, alpha1, alpha2, alpha3, beta0, beta1, beta2, beta3 = iono

    df = eph[keys].to_dataframe()

    df["alpha0"] = alpha0
    df["alpha1"] = alpha1
    df["alpha2"] = alpha2
    df["alpha3"] = alpha3
    df["beta0"]  = beta0
    df["beta1"]  = beta1
    df["beta2"]  = beta2
    df["beta3"]  = beta3

    iono = nav.attrs["ionospheric_corr_GPS"]
    cols = ["alpha0","alpha1","alpha2","alpha3","beta0","beta1","beta2","beta3"]
    df[cols] = iono  # broadcasts across all rows

    # Add UTC / leap second parameters as constant columns
    df["A0"]     = utc["A0"]
    df["A1"]     = utc["A1"]
    df["tot"]    = utc["tot"]
    df["WNt"]    = utc["WNt"]
    df["dtLS"]   = utc["dtLS"]
    df["dtLSF"]  = utc["dtLSF"]
    df["WNLSF"]  = utc["WNLSF"]
    df["DN"]     = utc["DN"]

    row = df.dropna(subset=["Toe"]).iloc[1]
    eph.to_dataframe().columns

    clean_df = df.dropna(subset=["Toe"]).query("TransTime < 604800")
    rows = []
    #print(i)
    for i in range(len(clean_df.dropna(subset=["Toe"]))):
        row = clean_df.iloc[i]
        params = {
            "sqrtA": row["sqrtA"],
            "e": row["Eccentricity"],
            "i0": row["Io"],
            "Omega0": row["Omega0"],
            "omega": row["omega"],
            "M0": row["M0"],
            "Toe": row["Toe"],
            "DeltaN": row["DeltaN"],
            "Cuc": row["Cuc"],
            "Cus": row["Cus"],
            "Cic": row["Cic"],
            "Cis": row["Cis"],
            "Crc": row["Crc"],
            "Crs": row["Crs"],
            "OmegaDot": row["OmegaDot"],
            "IDOT": row["IDOT"],
            "af0": row["SVclockBias"],
            "af1": row["SVclockDrift"],
            "af2": row["SVclockDriftRate"],
            "TGD": row["TGD"],
            "FitIntvl": row["FitIntvl"],
            "IODE": row["IODE"],
            "TOW": row["TransTime"],
            "GPSWeek": row["GPSWeek"],
            "IODC": row["IODC"],
            "URAIdx": row["SVacc"],
            "deltai": row["Io"],
            "TOA": row["Toe"],
            "alpha0": row["alpha0"],
            "alpha1": row["alpha1"],
            "alpha2": row["alpha2"],
            "alpha3": row["alpha3"],
            "beta0": row["beta0"],
            "beta1": row["beta1"],
            "beta2": row["beta2"],
            "beta3": row["beta3"],
            "A0" : row["A0"],
            "A1" : row["A1"],
            "tot" : row["tot"],
            "WNt" : row["WNt"],
            "dtLS" : row["dtLS"],
            "dtLSF" : row["dtLSF"],
            "WNLSF" : row["WNLSF"],
            "DN" : row["DN"],
            "WNa": row["GPSWeek"],
            "time": row.name,
        
        }


        encoded=encode_gps_lnav_ephemeris(params)

        rows.append({
            "sqrtA": row["sqrtA"],
            "e": row["Eccentricity"],
            "i0": row["Io"],
            "Omega0": row["Omega0"],
            "omega": row["omega"],
            "M0": row["M0"],
            "Toe": row["Toe"],
            "DeltaN": row["DeltaN"],
            "Cuc": row["Cuc"],
            "Cus": row["Cus"],
            "Cic": row["Cic"],
            "Cis": row["Cis"],
            "Crc": row["Crc"],
            "Crs": row["Crs"],
            "OmegaDot": row["OmegaDot"],
            "IDOT": row["IDOT"],
            "af0": row["SVclockBias"],
            "af1": row["SVclockDrift"],
            "af2": row["SVclockDriftRate"],
            "TGD": row["TGD"],
            "FitIntvl": row["FitIntvl"],
            "IODE": row["IODE"],
            "TOW": row["TransTime"],
            "GPSWeek": row["GPSWeek"],
            "IODC": row["IODC"],
            "URAIdx": row["SVacc"],
            "deltai": row["Io"],
            "TOA": row["Toe"],
            "alpha0": row["alpha0"],
            "alpha1": row["alpha1"],
            "alpha2": row["alpha2"],
            "alpha3": row["alpha3"],
            "beta0": row["beta0"],
            "beta1": row["beta1"],
            "beta2": row["beta2"],
            "beta3": row["beta3"],
            "A0" : row["A0"],
            "A1" : row["A1"],
            "tot" : row["tot"],
            "WNt" : row["WNt"],
            "dtLS" : row["dtLS"],
            "dtLSF" : row["dtLSF"],
            "WNLSF" : row["WNLSF"],
            "DN" : row["DN"],
            "WNa": row["GPSWeek"],
            "time": row.name,
            "encoded":encoded
        })

        
        #print(encode_gps_lnav_ephemeris(params))
    
        tables[sv] = pd.DataFrame(rows)

# Dictionary med SV/PRN-numre og tilhørende page numbers

SV_page_subframe4 = {2: 25,
                     3: 26,
                     4: 27,
                     5: 28,
                     7: 29,
                     8: 30,
                     9: 31,
                     10: 32}

SV_page_subframe5 = {1: 1,
                     2: 2,
                     3: 3,
                     4: 4,
                     5: 5,
                     6: 6,
                     7: 7,
                     8: 8,
                     9: 9,
                     10: 10,
                     11: 11,
                     12: 12,
                     13: 13,
                     14: 14,
                     15: 15,
                     16: 16,
                     17: 17,
                     18: 18,
                     19: 19,
                     20: 20,
                     21: 21,
                     22: 22,
                     23: 23,
                     24: 24
                     }
SV_input_dict = {
                1: "G01",
                2: "G02",
                3: "G03",
                4: "G04",
                5: "G05",
                6: "G06",
                7: "G07",
                8: "G08",
                9: "G09",
                10: "G10",
                11: "G11",
                12: "G12",
                13: "G13",
                14: "G14",
                15: "G15",
                16: "G16",
                17: "G17",
                18: "G18",
                19: "G19",
                20: "G20",
                21: "G21",
                22: "G22",
                23: "G23",
                24: "G24",
                25: "G25",
                26: "G26",
                27: "G27",
                28: "G28",
                29: "G29",
                30: "G30",
                31: "G31",
                32: "G32",
}

def solve_kepler_E(Mk, e, tol=1e-12, max_iter=50):
    """
    Solve Kepler's equation for eccentric anomaly E:
        Mk = E - e*sin(E)
    Inputs
      Mk : mean anomaly (rad). scalar or numpy array
      e  : eccentricity (0 <= e < 1). scalar or array-broadcastable to Mk
    Returns
      E  : eccentric anomaly (rad), same shape as Mk
    """
    Mk = np.asarray(Mk, dtype=float)
    e = np.asarray(e, dtype=float)

    # Wrap Mk to [-pi, pi] for better convergence
    M = (Mk + np.pi) % (2*np.pi) - np.pi

    # Initial guess (good for GNSS-like small e)
    E = M.copy()
    # Optional: slightly better guess when e is not tiny
    E = np.where(e > 0.8, np.pi * np.sign(M), E)

    for _ in range(max_iter):
        f = E - e * np.sin(E) - M
        fp = 1.0 - e * np.cos(E)

        dE = -f / fp
        E = E + dE

        if np.all(np.abs(dE) < tol):
            break
    else:
        raise RuntimeError("Kepler solver did not converge")

    # Unwrap back to same "branch" as original Mk (optional)
    # Return E in [0, 2pi) if you prefer:
    # E = E % (2*np.pi)

    return E

def R1(theta):
    return np.array([
        [1, 0, 0],
        [0, np.cos(theta), np.sin(theta)],
        [0, -np.sin(theta), np.cos(theta)]
    ])

def R3(theta):
    return np.array([
        [np.cos(theta), np.sin(theta), 0],
        [-np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])


def ehpm_to_ECEFlocation(SV):
    #constant
    mu=3.986005*10**14 #m^3/s^2  earth grav const for gps user
    omegaDot_e=7.2921151467*10**-5 # rad/sec earth rotaion rate
    M_o=tables[SV_input_dict[SV]]["M0"][0]
    Deltan=tables[SV_input_dict[SV]]["DeltaN"][0]
    a=tables[SV_input_dict[SV]]["sqrtA"][0]**2
    e=tables[SV_input_dict[SV]]["e"][0]
    w=tables[SV_input_dict[SV]]["omega"][0]
    C_uc=tables[SV_input_dict[SV]]["Cuc"][0]
    C_us=tables[SV_input_dict[SV]]["Cus"][0]
    C_rs=tables[SV_input_dict[SV]]["Crs"][0]
    C_rc=tables[SV_input_dict[SV]]["Crc"][0]
    i_0 = tables[SV_input_dict[SV]]["i0"][0]
    i_dot = tables[SV_input_dict[SV]]["IDOT"][0]
    C_ic = tables[SV_input_dict[SV]]["Cic"][0]
    C_is = tables[SV_input_dict[SV]]["Cis"][0]
    Omega0 = tables[SV_input_dict[SV]]["Omega0"][0]
    OmegaDot = tables[SV_input_dict[SV]]["OmegaDot"][0]
    t=tables[SV_input_dict[SV]]["TOW"][0]
    t_oe=tables[SV_input_dict[SV]]["Toe"][0]

    #compute t_k
    t_k=t-t_oe
    if t_k > 302400:
        t_k-=604800
    elif t_k < -302400:
        t_k +=604800

    #compute mean anomaly fo t_k
    M_k=M_o+((np.sqrt(mu)/(np.sqrt(a**3)))+Deltan)*t_k

    E_k=solve_kepler_E(M_k,e)   #rad
    
    v_k = np.arctan2(np.sqrt(1 - e**2) * np.sin(E_k),
                 np.cos(E_k) - e)
    
    u_k=w+v_k+C_uc*np.cos(2*(w+v_k))+C_us*np.sin(2*(w+v_k))

    r_k=a*(1-e*np.cos(E_k))+C_rc*np.cos(2*(w+v_k))+C_rs*np.sin(2*(w+v_k))

    i_k = i_0 + i_dot * t_k + C_ic * np.cos(2 * (w + v_k)) + C_is * np.sin(2*(w + v_k))     # rad

    lambda_k = Omega0 + (OmegaDot - omegaDot_e)*t_k-omegaDot_e* t_oe

    rk_vec = np.array([r_k, 0, 0])

    XYZ = R3(-lambda_k) @ R1(-i_k) @ R3(-u_k) @ rk_vec

    return XYZ




def ECEF(N: float, E: float, h: float):  
    
    a = 6378137.0                       # Halv storakse (Jordens radius)
    f = 1 / 300                         # fra PP (GP2), flattening
    e = np.sqrt(2*f - f**2)       
    Nbar = a / (np.sqrt(1 - e**2*(np.sin(np.radians(N)))**2))


    # Cartesian (ECEF) coordinates in radians
    X = (Nbar + h) * np.cos(np.radians(N)) * np.cos(np.radians(E))
    Y = (Nbar + h) * np.cos(np.radians(N)) * np.sin(np.radians(E))
    Z = (Nbar * (1 - e**2) + h) * np.sin(np.radians(N))


    return X, Y, Z

def paddelay(SV: int ,location: tuple):
    distnace_to_sat=np.sqrt(sum((ehpm_to_ECEFlocation(SV)-ECEF(55.738957, 12.500242, 20))**2))
    return round(distnace_to_sat/(3*10**8)*1000*1023) #1000 sec to ms, 1023 prn code length

Z_count_start = tables["G01"]["encoded"][0]["TOW"].n          # Encoded: Binær


def subframe(subframe_number, page_number, SV, Z_count: int):
    """If subframe is 1-3 set page_number = 0"""

    # Subframe 1
    if subframe_number == 1 and page_number == 0:
        words1_24 = []

        # Word 1
        preamble = [1,0,0,0,1,0,1,1]
        TLM = bitarray(14)                                  
        ISF = bitarray([1])                                                                     # Integrity Status Flag
        reserved = bitarray(1)
        
        word1_1 = bitarray(0)
        word1_1.extend(preamble) 
        word1_1 += TLM                                                                          # for PPS and CS
        word1_1.extend(ISF)
        word1_1 += reserved

        words1_24.append(word1_1)

        # Word 2
        TOW17 = bitarray(int_to_bits(Z_count, 17))                                              # First 17 bits of TOW (19 bits long in total)
        TOW18 = bitarray([0])                                                                   # 1: User Range Accuracy (URA) may be worse than indicated in NAV message
        TOW19 = bitarray([1])                                                                   # 1: Anti-spoof for the SV is turned ON
        TOW = bitarray(0)
        TOW.extend(TOW17)
        TOW.extend(TOW18)
        TOW.extend(TOW19)                                                                       #  Create full 19-bit TOW
        subframe_ID = bitarray([0, 0, 1]) 
        # t tilføjes i parity-funktion

        word2_1 = bitarray(0)
        word2_1.extend(TOW)
        word2_1.extend(subframe_ID)

        words1_24.append(word2_1)

        # Word 3
        GPS_week = tables[SV_input_dict[SV]]["encoded"][0]["GPSWeek"].bits                                                                 # Current GPS week number
        code_flag = [1, 0]
        URA_index = tables[SV_input_dict[SV]]["encoded"][0]["URAIdx"].bits                      # Ideal: 0000
        SV_health = bitarray(6)                                                                 # Healthy: 000000
        IODC = tables[SV_input_dict[SV]]["encoded"][0]["IODC"].bits[:2]                         # First 2 bits of IODC, the rest (8 bits) in word 8
        

        word3_1 = bitarray(0)
        word3_1.extend(GPS_week)
        word3_1.extend(code_flag)
        word3_1.extend(URA_index)
        word3_1.extend(SV_health)
        word3_1.extend(IODC)

        words1_24.append(word3_1)

        # Word 4
        MSB = [0]
        reserved = bitarray(23)

        word4_1 = bitarray(0)
        word4_1.extend(MSB)
        word4_1 +=  reserved

        words1_24.append(word4_1)

        # Word 5
        reserved = bitarray(24)

        word5_1 = bitarray(0)
        word5_1 += reserved

        words1_24.append(word5_1)

        # Word 6
        reserved = bitarray(24)

        word6_1 = bitarray(0)
        word6_1 += reserved

        words1_24.append(word6_1)

        # Word 7
        reserved = bitarray(16)
        T_GD = tables[SV_input_dict[SV]]["encoded"][0]["TGD"].bits                               # Estimated group delay

        word7_1 = bitarray(0)
        word7_1.extend(reserved)
        word7_1.extend(T_GD) 

        words1_24.append(word7_1)

        # Word 8
        IODC = tables[SV_input_dict[SV]]["encoded"][0]["IODC"].bits[2:]                          # The rest of the IODC from word 3
        t_OC = tables[SV_input_dict[SV]]["encoded"][0]["Toc"].bits

        word8_1 = bitarray(0)
        word8_1.extend(IODC)
        word8_1.extend(t_OC)

        words1_24.append(word8_1)

        # Word 9
        af2 = tables[SV_input_dict[SV]]["encoded"][0]["af2"].bits                               # Second order clock correction coefficient? er bare 0'er
        af1 = tables[SV_input_dict[SV]]["encoded"][0]["af1"].bits                               # First-order clock correction coefficient

        word9_1 = bitarray(0)
        word9_1.extend(af2) 
        word9_1.extend(af1)

        words1_24.append(word9_1)

        # Word 10
        af0 = tables[SV_input_dict[SV]]["encoded"][0]["af0"].bits                               # Constant clock correction coefficient
        # t tilføjes i parity-funktion                                                          # Noninformation bearing bits used for parity correction

        word10_1 = bitarray(0)
        word10_1.extend(af0)

        words1_24.append(word10_1)

        return words1_24, Z_count
        
    # Subframe 2
    if subframe_number == 2 and page_number == 0:
        words2_24 = []

        # Word 1
        preamble = [1,0,0,0,1,0,1,1]
        TLM = bitarray(14)                              
        ISF = [1]                                        
        reserved = bitarray(1)
        
        word1_2 = bitarray(0)
        word1_2.extend(preamble) 
        word1_2.extend(TLM)           
        word1_2.extend(ISF)
        word1_2.extend(reserved)

        words2_24.append(word1_2)

        # Word 2
        TOW17 = bitarray(int_to_bits(Z_count, 17))                                              # First 17 bits of TOW (19 bits long in total)
        TOW18 = bitarray([0])                                                                   # 1: User Range Accuracy (URA) may be worse than indicated in NAV message
        TOW19 = bitarray([1])                                                                   # 1: Anti-spoof for the SV is turned ON
        TOW = bitarray(0)
        TOW.extend(TOW17)
        TOW.extend(TOW18)
        TOW.extend(TOW19)                 

        subframe_ID = bitarray([0, 1, 0]) 
        # t tilføjes i parity-funktion    

        word2_2 = bitarray(0)
        word2_2.extend(TOW)
        word2_2.extend(subframe_ID)

        words2_24.append(word2_2)

        # Word 3
        IODE = tables[SV_input_dict[SV]]["encoded"][0]["IODE"].bits                             # Issue of data Ephemeris
        C_rs = tables[SV_input_dict[SV]]["encoded"][0]["Crs"].bits                              # Radius correction

        word3_2 = bitarray(0)
        word3_2.extend(IODE)
        word3_2.extend(C_rs)

        words2_24.append(word3_2)

        # Word 4
        delta_n = tables[SV_input_dict[SV]]["encoded"][0]["DeltaN"].bits                        # Mean motion difference
        M0_MSB = tables[SV_input_dict[SV]]["encoded"][0]["M0"].bits[:8]                         # First 8 bits of mean anomaly

        word4_2 = bitarray(0)
        word4_2.extend(delta_n)
        word4_2.extend(M0_MSB)

        words2_24.append(word4_2)

        # Word 5
        M0_LSB = tables[SV_input_dict[SV]]["encoded"][0]["M0"].bits[8:]                         # Last 24 bits of mean anomaly

        word5_2 = bitarray(0)
        word5_2.extend(M0_LSB)

        words2_24.append(word5_2)

        # Word 6
        C_uc = tables[SV_input_dict[SV]]["encoded"][0]["Cuc"].bits                              # Latitude correction
        e_MSB = tables[SV_input_dict[SV]]["encoded"][0]["Eccentricity"].bits[:8]                # Eccentricity, first 8 bits

        word6_2 = bitarray(0)
        word6_2.extend(C_uc)
        word6_2.extend(e_MSB)

        words2_24.append(word6_2)

        # Word 7
        e_LSB = tables[SV_input_dict[SV]]["encoded"][0]["Eccentricity"].bits[8:]              # Last 24 bits of eccentricity

        word7_2 = bitarray(0)
        word7_2.extend(e_LSB)

        words2_24.append(word7_2)

        # Word 8
        C_us = tables[SV_input_dict[SV]]["encoded"][0]["Cus"].bits                            # Latitude correction
        sqrtA_MSB = tables[SV_input_dict[SV]]["encoded"][0]["sqrtA"].bits[:8]                 # First 8 bits of sqrtA (semi-major axis)

        word8_2 = bitarray(0)
        word8_2.extend(C_us)
        word8_2.extend(sqrtA_MSB)

        words2_24.append(word8_2)

        # Word 9
        sqrtA_LSB = tables[SV_input_dict[SV]]["encoded"][0]["sqrtA"].bits[8:]                 # Last 24 bits of sqrtA (semi-major axis)

        word9_2 = bitarray(0)
        word9_2.extend(sqrtA_LSB)

        words2_24.append(word9_2)

        # Word 10
        t_oe = tables[SV_input_dict[SV]]["encoded"][0]["Toe"].bits                            # Ephemeris data
        FIF = tables[SV_input_dict[SV]]["encoded"][0]["FitIntvl"].bits                        # Fit Interval Flag
        AODO = "00000"                                                                        # Age of Data Offset
        # t tilføjes i parity-funktion

        word10_2 = bitarray()
        word10_2.extend(t_oe)
        word10_2.extend(FIF)
        word10_2.extend(AODO)

        words2_24.append(word10_2)

        return words2_24, Z_count

    # Subframe 3
    if subframe_number == 3 and page_number == 0:
        words3_24 = []

        # Word 1
        preamble = [1,0,0,0,1,0,1,1]
        TLM = bitarray(14)      
        ISF = [1]               
        reserved = bitarray(1)
        
        word1_3 = bitarray(0)
        word1_3.extend(preamble) 
        word1_3 += TLM           
        word1_3.extend(ISF)
        word1_3 += reserved

        words3_24.append(word1_3)

        # Word 2
        TOW17 = bitarray(int_to_bits(Z_count, 17))                      # First 17 bits of TOW (19 bits long in total)
        TOW18 = bitarray([0])                                           # 1: User Range Accuracy (URA) may be worse than indicated in NAV message
        TOW19 = bitarray([1])                                           # 1: Anti-spoof for the SV is turned ON
        TOW = bitarray(0)
        TOW.extend(TOW17)
        TOW.extend(TOW18)
        TOW.extend(TOW19)                  
        subframe_ID = bitarray([0, 1, 1]) 
        # t tilføjes i parity-funktion    

        word2_3 = bitarray(0)
        word2_3.extend(TOW)
        word2_3.extend(subframe_ID)

        words3_24.append(word2_3)

        # Word 3
        C_ic = tables[SV_input_dict[SV]]["encoded"][0]["Cic"].bits
        Omega0_MSB = tables[SV_input_dict[SV]]["encoded"][0]["Omega0"].bits[:8]              # First 8 bits, ascending node

        word3_3 = bitarray(0)
        word3_3.extend(C_ic)
        word3_3.extend(Omega0_MSB)

        words3_24.append(word3_3)

        # Word 4
        Omega0_LSB = tables[SV_input_dict[SV]]["encoded"][0]["Omega0"].bits[8:]              # Last 24 bits of ascending node

        word4_3 = bitarray(0)
        word4_3.extend(Omega0_LSB)

        words3_24.append(word4_3)

        # Word 5
        C_is = tables[SV_input_dict[SV]]["encoded"][0]["Cis"].bits
        i0 = tables[SV_input_dict[SV]]["encoded"][0]["Io"].bits[:8]                         # First 8 bits of inclination angle

        word5_3 = bitarray(0)
        word5_3.extend(C_is)
        word5_3.extend(i0)

        words3_24.append(word5_3)

        # Word 6
        i0 = tables[SV_input_dict[SV]]["encoded"][0]["Io"].bits[8:]                        # Last 24-bits of inclination angle

        word6_3 = bitarray(0)
        word6_3.extend(i0)

        words3_24.append(word6_3)

        # Word 7
        C_rc = tables[SV_input_dict[SV]]["encoded"][0]["Crc"].bits
        w = tables[SV_input_dict[SV]]["encoded"][0]["omega"].bits[:8]                      # First 8 bits of omega (argument of perigee)

        word7_3 = bitarray(0)
        word7_3.extend(C_rc)
        word7_3.extend(w)

        words3_24.append(word7_3)

        # Word 8
        w = tables[SV_input_dict[SV]]["encoded"][0]["omega"].bits[8:]                      # Last 24 bits of argument of perigee

        word8_3 = bitarray(0)
        word8_3.extend(w)

        words3_24.append(word8_3)

        # Word 9 
        Omega_dot = tables[SV_input_dict[SV]]["encoded"][0]["OmegaDot"].bits               # Rate of node's right ascension

        word9_3 = bitarray(0)
        word9_3.extend(Omega_dot)

        words3_24.append(word9_3)

        # Word 10
        IODE = tables[SV_input_dict[SV]]["encoded"][0]["IODE"].bits                       # Issue of Data Ephemeris
        IDOT = tables[SV_input_dict[SV]]["encoded"][0]["IDOT"].bits                       # Rate of inclination angle
        # t tilføjes i parity-funktion

        word10_3 = bitarray(0)
        word10_3.extend(IODE)
        word10_3.extend(IDOT)

        words3_24.append(word10_3)

        return words3_24, Z_count

    # Subframe 4, almanac
    if subframe_number == 4: 
        if page_number in [2, 3, 4, 5, 7, 8, 9, 10]:                        # Almanac (lavet efter Figure 20-1 data format (sheet 4 of 11))
            words4_24_alm = []                                              # Initialize list for 10 24-bit words. words[subframe]_24

            # Word 1
            preamble = [1,0,0,0,1,0,1,1]
            TLM = bitarray(14)                              
            ISF = bitarray([1])                                       
            reserved = bitarray(1)
            
            word1_4_alm = bitarray(0)
            word1_4_alm.extend(preamble)                          
            word1_4_alm += TLM                                    
            word1_4_alm.extend(ISF)
            word1_4_alm += reserved

            words4_24_alm.append(word1_4_alm)

            # Word 2
            TOW17 = bitarray(int_to_bits(Z_count, 17))                      # First 17 bits of TOW (19 bits long in total)
            TOW18 = bitarray([0])                                           # 1: User Range Accuracy (URA) may be worse than indicated in NAV message
            TOW19 = bitarray([1])                                           # 1: Anti-spoof for the SV is turned ON
            TOW = bitarray(0)
            TOW.extend(TOW17)
            TOW.extend(TOW18)
            TOW.extend(TOW19)                 

            subframe_ID = bitarray([1, 0, 0]) 
            # t tilføjes i parity-funktion               

            word2_4_alm = bitarray(0)
            word2_4_alm.extend(TOW)
            word2_4_alm.extend(subframe_ID)

            words4_24_alm.append(word2_4_alm)

            if SV_input_dict[SV_page_subframe5[page_number]] in tables:         # Error handling: If a satellite does not exist in the data-set

                # Word 3
                data_ID = "01" 
                SV_ID = int_to_bits(SV_page_subframe4[page_number],6)
                e = tables[SV_input_dict[SV_page_subframe4[page_number]]]["encoded"][0]["Eccentricity"].bits[:16]      

                word3_4_alm = bitarray(0)
                word3_4_alm.extend(data_ID)
                word3_4_alm.extend(SV_ID)
                word3_4_alm.extend(e)

                words4_24_alm.append(word3_4_alm)

                # Word 4
                t_oa = tables[SV_input_dict[SV_page_subframe4[page_number]]]["encoded"][0]["TOA"].bits
                delta_i = tables[SV_input_dict[SV_page_subframe4[page_number]]]["encoded"][0]["deltai"].bits

                word4_4_alm = bitarray(0)
                word4_4_alm.extend(t_oa)
                word4_4_alm.extend(delta_i)

                words4_24_alm.append(word4_4_alm)

                # Word 5
                Omega_dot = tables[SV_input_dict[SV_page_subframe4[page_number]]]["encoded"][0]["OmegaDot"].bits[:16]
                SV_health = "00000000" 

                word5_4_alm = bitarray(0)
                word5_4_alm.extend(Omega_dot)
                word5_4_alm.extend(SV_health)

                words4_24_alm.append(word5_4_alm)

                # Word 6
                sqrtA = tables[SV_input_dict[SV_page_subframe4[page_number]]]["encoded"][0]["sqrtA"].bits[:24]

                word6_4_alm = bitarray(0)
                word6_4_alm.extend(sqrtA)

                words4_24_alm.append(word6_4_alm)

                # Word 7
                Omega0 = tables[SV_input_dict[SV_page_subframe4[page_number]]]["encoded"][0]["Omega0"].bits[:24]

                word7_4_alm = bitarray(0)
                word7_4_alm.extend(Omega0)

                words4_24_alm.append(word7_4_alm)

                # Word 8
                w = tables[SV_input_dict[SV_page_subframe4[page_number]]]["encoded"][0]["omega"].bits[:24]          # omega

                word8_4_alm = bitarray(0)
                word8_4_alm.extend(w)

                words4_24_alm.append(word8_4_alm)

                # Word 9
                M0 = tables[SV_input_dict[SV_page_subframe4[page_number]]]["encoded"][0]["M0"].bits[:24]

                word9_4_alm = bitarray(0)
                word9_4_alm.extend(M0)

                words4_24_alm.append(word9_4_alm)

                # Word 10
                af0_MSB = tables[SV_input_dict[SV_page_subframe4[page_number]]]["encoded"][0]["af0"].bits[:8]
                af1 = tables[SV_input_dict[SV_page_subframe4[page_number]]]["encoded"][0]["af1"].bits[:11]
                af0_LSB = tables[SV_input_dict[SV_page_subframe4[page_number]]]["encoded"][0]["af0"].bits[8:11]
                # t tilføjes i parity-funktion

                word10_4_alm = bitarray(0)
                word10_4_alm.extend(af0_MSB)
                word10_4_alm.extend(af1)
                word10_4_alm.extend(af0_LSB)

                words4_24_alm.append(word10_4_alm)  
            
                return words4_24_alm, Z_count
            
            else:

                # Word 3
                data_ID = "01" 
                SV_ID = int_to_bits(SV_page_subframe4[page_number],6)
                e = bitarray(16)  

                word3_4_alm = bitarray(0)
                word3_4_alm.extend(data_ID)
                word3_4_alm.extend(SV_ID)
                word3_4_alm.extend(e)

                words4_24_alm.append(word3_4_alm)

                # Word 4
                t_oa = bitarray(8) 
                delta_i = bitarray(16) 

                word4_4_alm = bitarray(0)
                word4_4_alm.extend(t_oa)
                word4_4_alm.extend(delta_i)

                words4_24_alm.append(word4_4_alm)

                # Word 5
                Omega_dot = bitarray(16) 
                SV_health = "00000000" 

                word5_4_alm = bitarray(0)
                word5_4_alm.extend(Omega_dot)
                word5_4_alm.extend(SV_health)

                words4_24_alm.append(word5_4_alm)

                # Word 6
                sqrtA = bitarray(24) 

                word6_4_alm = bitarray(0)
                word6_4_alm.extend(sqrtA)

                words4_24_alm.append(word6_4_alm)

                # Word 7
                Omega0 = bitarray(24) 

                word7_4_alm = bitarray(0)
                word7_4_alm.extend(Omega0)

                words4_24_alm.append(word7_4_alm)

                # Word 8
                w = bitarray(24)          # omega

                word8_4_alm = bitarray(0)
                word8_4_alm.extend(w)

                words4_24_alm.append(word8_4_alm)

                # Word 9
                M0 = bitarray(24) 

                word9_4_alm = bitarray(0)
                word9_4_alm.extend(M0)

                words4_24_alm.append(word9_4_alm)

                # Word 10
                af0_MSB = bitarray(8) 
                af1 = bitarray(11) 
                af0_LSB = bitarray(3) 
                # t tilføjes i parity-funktion

                word10_4_alm = bitarray(0)
                word10_4_alm.extend(af0_MSB)
                word10_4_alm.extend(af1)
                word10_4_alm.extend(af0_LSB)

                words4_24_alm.append(word10_4_alm)
            
                return words4_24_alm, Z_count
            
        
        # Subframe 4, reserved
        elif page_number in [1, 6, 11, 16, 21]:
            words4_24_res1 = []

            # Word 1
            preamble = [1,0,0,0,1,0,1,1]
            TLM = bitarray(14)                              
            ISF = bitarray([1])                                       
            reserved = bitarray(1)
            
            word1_4_res1 = bitarray(0)
            word1_4_res1.extend(preamble)                          
            word1_4_res1 += TLM                                    
            word1_4_res1.extend(ISF)
            word1_4_res1 += reserved

            words4_24_res1.append(word1_4_res1)

            # Word 2
            TOW17 = bitarray(int_to_bits(Z_count, 17))                      
            TOW18 = bitarray([0])                                        
            TOW19 = bitarray([1])                                        
            TOW = bitarray(0)
            TOW.extend(TOW17)
            TOW.extend(TOW18)
            TOW.extend(TOW19)                 

            subframe_ID = bitarray([1, 0, 0]) 
            # t tilføjes i parity-funktion                

            word2_4_res1 = bitarray(0)
            word2_4_res1.extend(TOW)
            word2_4_res1.extend(subframe_ID)

            words4_24_res1.append(word2_4_res1)

            # Word 3
            data_ID_res1 = "01" 
            SV_page_ID = int_to_bits(page_number,6) 
            res1 = bitarray(16) 

            word3_4_res1 = bitarray(0)
            word3_4_res1.extend(data_ID_res1)
            word3_4_res1.extend(SV_page_ID)
            word3_4_res1 += res1

            words4_24_res1.append(word3_4_res1)

            # Word 4
            res2 = bitarray(24) 

            word4_4_res1 = bitarray(0)
            word4_4_res1 += res2

            words4_24_res1.append(word4_4_res1)

            # Word 5
            res3 = bitarray(24)

            word5_4_res1 = bitarray(0)
            word5_4_res1 += res3

            words4_24_res1.append(word5_4_res1)

            # Word 6
            res4 = bitarray(24)

            word6_4_res1 = bitarray(0)
            word6_4_res1 += res4

            words4_24_res1.append(word6_4_res1)

            # Word 7
            res5 = bitarray(24)

            word7_4_res1 = bitarray(0)
            word7_4_res1 += res5

            words4_24_res1.append(word7_4_res1)

            # Word 8
            res6 = bitarray(24)

            word8_4_res1 = bitarray(0)
            word8_4_res1 += res6

            words4_24_res1.append(word8_4_res1)

            # Word 9
            res7 = bitarray(8)
            res8 = bitarray(16)

            word9_4_res1 = bitarray(0)
            word9_4_res1 += res7 + res8

            words4_24_res1.append(word9_4_res1)

            # Word 10
            res9 = bitarray(22)
            # t tilføjes i parity-funktion

            word10_4_res1 = bitarray(0)
            word10_4_res1 += res9 

            words4_24_res1.append(word10_4_res1)

            return words4_24_res1, Z_count
        
        # Subframe 4, reserved
        elif page_number in [12, 19, 20, 22, 23, 24]:
            words4_24_res2 = []

            # Word 1
            preamble = [1,0,0,0,1,0,1,1]
            TLM = bitarray(14)                              
            ISF = bitarray([1])                                       
            reserved = bitarray(1)
            
            word1_4_res2 = bitarray(0)
            word1_4_res2.extend(preamble)                          
            word1_4_res2 += TLM                                    
            word1_4_res2.extend(ISF)
            word1_4_res2 += reserved

            words4_24_res2.append(word1_4_res2)

            # Word 2
            TOW17 = bitarray(int_to_bits(Z_count, 17))                      
            TOW18 = bitarray([0])                                        
            TOW19 = bitarray([1])                                        
            TOW = bitarray(0)
            TOW.extend(TOW17)
            TOW.extend(TOW18)
            TOW.extend(TOW19)                 

            subframe_ID = bitarray([1, 0, 0]) 
            # t tilføjes i parity-funktion                

            word2_4_res2 = bitarray(0)
            word2_4_res2.extend(TOW)
            word2_4_res2.extend(subframe_ID)

            words4_24_res2.append(word2_4_res2)

            # Word 3
            data_ID_res2 = "01"
            SV_page_ID_res2 = int_to_bits(page_number,6) 
            res10 = bitarray(16)

            word3_4_res2 = bitarray(0)
            word3_4_res2.extend(data_ID_res2)
            word3_4_res2.extend(SV_page_ID_res2)
            word3_4_res2 += res10

            words4_24_res2.append(word3_4_res2)

            # Word 4
            res11 = bitarray(24)

            word4_4_res2 = bitarray(0)
            word4_4_res2 += res11

            words4_24_res2.append(word4_4_res2)

            # Word 5
            res12 = bitarray(24)

            word5_4_res2 = bitarray(0)
            word5_4_res2 += res12

            words4_24_res2.append(word5_4_res2)

            # Word 6
            res13 = bitarray(24)

            word6_4_res2 = bitarray(0)
            word6_4_res2 += res13

            words4_24_res2.append(word6_4_res2)

            # Word 7
            res14 = bitarray(24)

            word7_4_res2 = bitarray(0)
            word7_4_res2 += res14

            words4_24_res2.append(word7_4_res2)

            # Word 8
            res15 = bitarray(24)

            word8_4_res2 = bitarray(0)
            word8_4_res2 += res15

            words4_24_res2.append(word8_4_res2)

            # Word 9
            res16 = bitarray(8)
            res17 = bitarray(16)

            word9_4_res2 = bitarray(0)
            word9_4_res2 += res16 + res17

            words4_24_res2.append(word9_4_res2)

            # Word 10
            res18 = bitarray(22)
            # t tilføjes i parity-funktion

            word10_4_res2 = bitarray(0)
            word10_4_res2 += res18 

            words4_24_res2.append(word10_4_res2)

            return words4_24_res2, Z_count
        
        # Subframe 4, page 18
        elif page_number == 18:
            words4_24_18 = []

            # Word 1
            preamble = [1,0,0,0,1,0,1,1]
            TLM = bitarray(14)                              
            ISF = bitarray([1])                                       
            reserved = bitarray(1)
            
            word1_4_18 = bitarray(0)
            word1_4_18.extend(preamble)                          
            word1_4_18 += TLM                                    
            word1_4_18.extend(ISF)
            word1_4_18 += reserved

            words4_24_18.append(word1_4_18)

            # Word 2
            TOW17 = bitarray(int_to_bits(Z_count, 17))                      
            TOW18 = bitarray([0])                                        
            TOW19 = bitarray([1])                                        
            TOW = bitarray(0)
            TOW.extend(TOW17)
            TOW.extend(TOW18)
            TOW.extend(TOW19)                 

            subframe_ID = bitarray([1, 0, 0]) 
            # t tilføjes i parity-funktion               

            word2_4_18 = bitarray(0)
            word2_4_18.extend(TOW)
            word2_4_18.extend(subframe_ID)

            words4_24_18.append(word2_4_18)

            # Word 3
            data_ID_18 = "01"
            SV_page_ID_18 = int_to_bits(page_number,6)
            alpha0 = tables[SV_input_dict[1]]["encoded"][0]["alpha0"].bits              # Atmosfære parametre er ens for alle
            alpha1 = tables[SV_input_dict[1]]["encoded"][0]["alpha1"].bits 

            word3_4_18 = bitarray(0)
            word3_4_18.extend(data_ID_18)
            word3_4_18.extend(SV_page_ID_18)
            word3_4_18.extend(alpha0)
            word3_4_18.extend(alpha1)

            words4_24_18.append(word3_4_18)

            # Word 4
            alpha2 = tables[SV_input_dict[1]]["encoded"][0]["alpha2"].bits
            alpha3 = tables[SV_input_dict[1]]["encoded"][0]["alpha3"].bits
            beta0 = tables[SV_input_dict[1]]["encoded"][0]["beta0"].bits

            word4_24_18 = bitarray(0)
            word4_24_18.extend(alpha2)
            word4_24_18.extend(alpha3)
            word4_24_18.extend(beta0)

            words4_24_18.append(word4_24_18)

            # Word 5
            beta1 = tables[SV_input_dict[1]]["encoded"][0]["beta1"].bits
            beta2 = tables[SV_input_dict[1]]["encoded"][0]["beta2"].bits
            beta3 = tables[SV_input_dict[1]]["encoded"][0]["beta3"].bits

            word5_4_18 = bitarray(0)
            word5_4_18.extend(beta1)
            word5_4_18.extend(beta2)
            word5_4_18.extend(beta3)

            words4_24_18.append(word5_4_18)

            # Word 6
            A1 = tables[SV_input_dict[1]]["encoded"][0]["A1"].bits[:24]

            word6_4_18 = bitarray(0)
            word6_4_18.extend(A1)

            words4_24_18.append(word6_4_18)

            # Word 7
            A0_MSB = tables[SV_input_dict[1]]["encoded"][0]["A0"].bits[:24]

            word7_4_18 = bitarray(0)
            word7_4_18.extend(A0_MSB)

            words4_24_18.append(word7_4_18)

            # Word 8
            A0_LSB = tables[SV_input_dict[1]]["encoded"][0]["A0"].bits[24:]
            t_ot = tables[SV_input_dict[1]]["encoded"][0]["tot"].bits
            WN_t = tables[SV_input_dict[1]]["encoded"][0]["WNt"].bits

            word8_4_18 = bitarray(0)
            word8_4_18.extend(A0_LSB)
            word8_4_18.extend(t_ot)
            word8_4_18.extend(WN_t)

            words4_24_18.append(word8_4_18)

            # Word 9
            delta_t_LS = tables[SV_input_dict[1]]["encoded"][0]["dtLS"].bits
            WN_LSF = tables[SV_input_dict[1]]["encoded"][0]["WNLSF"].bits
            DN = tables[SV_input_dict[1]]["encoded"][0]["DN"].bits

            word9_4_18 = bitarray(0)
            word9_4_18.extend(delta_t_LS)
            word9_4_18.extend(WN_LSF)
            word9_4_18.extend(DN)

            words4_24_18.append(word9_4_18)

            # Word 10
            delta_t_LSF = tables[SV_input_dict[1]]["encoded"][0]["dtLSF"].bits
            res19 = bitarray(14)
            # t tilføjes i parity-funktion

            word10_4_18 = bitarray(0)
            word10_4_18.extend(delta_t_LSF)
            word10_4_18.extend(res19)

            words4_24_18.append(word10_4_18)

            return words4_24_18, Z_count
        
        # Subframe 4, page 25
        elif page_number == 25:
            words4_24_25 = []

            # Word 1
            preamble = [1,0,0,0,1,0,1,1]
            TLM = bitarray(14)                              
            ISF = bitarray([1])                                       
            reserved = bitarray(1)
            
            word1_4_25 = bitarray(0)
            word1_4_25.extend(preamble)                          
            word1_4_25 += TLM                                    
            word1_4_25.extend(ISF)
            word1_4_25 += reserved

            words4_24_25.append(word1_4_25)

            # Word 2
            TOW17 = bitarray(int_to_bits(Z_count, 17))                      # First 17 bits of TOW (19 bits long in total)
            TOW18 = bitarray([0])                                           # 1: User Range Accuracy (URA) may be worse than indicated in NAV message
            TOW19 = bitarray([1])                                           # 1: Anti-spoof for the SV is turned ON
            TOW = bitarray(0)
            TOW.extend(TOW17)
            TOW.extend(TOW18)
            TOW.extend(TOW19)                 

            subframe_ID = bitarray([1, 0, 0]) 
            # t tilføjes i parity-funktion                

            word2_4_25 = bitarray(0)
            word2_4_25.extend(TOW)
            word2_4_25.extend(subframe_ID)

            words4_24_25.append(word2_4_25)

            # Word 3
            data_ID_25 = "01"
            SV_page_ID_25 = int_to_bits(page_number,6)
            AS1 = bitarray(16)                                              # page 119. 4 SVs per 16 AS bits, however they seem to be insignificant so we set it = 0. Can be modified later if needed

            word3_4_25 = bitarray(0)
            word3_4_25.extend(data_ID_25)
            word3_4_25.extend(SV_page_ID_25)
            word3_4_25 += AS1

            words4_24_25.append(word3_4_25)

            # Word 4
            AS2 = bitarray(24)

            word4_4_25 = bitarray(0)
            word4_4_25 += AS2

            words4_24_25.append(word4_4_25)

            # Word 5
            AS3 = bitarray(24)

            word5_4_25 = bitarray(0)
            word5_4_25 += AS3

            words4_24_25.append(word5_4_25)

            # Word 6
            AS4 = bitarray(24)

            word6_4_25 = bitarray(0)
            word6_4_25 += AS4

            words4_24_25.append(word6_4_25)

            # Word 7
            AS5 = bitarray(24)

            word7_4_25 = bitarray(0)
            word7_4_25 += AS5

            words4_24_25.append(word7_4_25)

            # Word 8
            AS6 = bitarray(16)
            res20 = bitarray(2)
            SV_25_health = "000000"

            word8_4_25 = bitarray(0)
            word8_4_25 += AS6 + res20
            word8_4_25.extend(SV_25_health)

            words4_24_25.append(word8_4_25)

            # Word 9
            SV_26_health = "000000"
            SV_27_health = "000000"
            SV_28_health = "000000"
            SV_29_health = "000000"

            word9_4_25 = bitarray(0)
            word9_4_25.extend(SV_26_health)
            word9_4_25.extend(SV_27_health)
            word9_4_25.extend(SV_28_health)
            word9_4_25.extend(SV_29_health)

            words4_24_25.append(word9_4_25)

            # Word 10
            SV_30_health = "000000"
            SV_31_health = "000000"
            SV_32_health = "000000"
            res21 = bitarray(4)
            # t tilføjes i parity-funktion

            word10_4_25 = bitarray(0)
            word10_4_25.extend(SV_30_health)
            word10_4_25.extend(SV_31_health)
            word10_4_25.extend(SV_32_health)
            word10_4_25 += res21 

            words4_24_25.append(word10_4_25)

            return words4_24_25, Z_count
        
        # Subframe 4, page 13
        elif page_number == 13:
            words4_24_13 = []

            # Word 1
            preamble = [1,0,0,0,1,0,1,1]
            TLM = bitarray(14)                              
            ISF = bitarray([1])                                       
            reserved = bitarray(1)
            
            word1_4_13 = bitarray(0)
            word1_4_13.extend(preamble)                          
            word1_4_13 += TLM                                    
            word1_4_13.extend(ISF)
            word1_4_13 += reserved

            words4_24_13.append(word1_4_13)

            # Word 2
            TOW17 = bitarray(int_to_bits(Z_count, 17))                      # First 17 bits of TOW (19 bits long in total)
            TOW18 = bitarray([0])                                           # 1: User Range Accuracy (URA) may be worse than indicated in NAV message
            TOW19 = bitarray([1])                                           # 1: Anti-spoof for the SV is turned ON
            TOW = bitarray(0)
            TOW.extend(TOW17)
            TOW.extend(TOW18)
            TOW.extend(TOW19)                 

            subframe_ID = bitarray([1, 0, 0]) 
            # t tilføjes i parity-funktion                

            word2_4_13 = bitarray(0)
            word2_4_13.extend(TOW)
            word2_4_13.extend(subframe_ID)

            words4_24_13.append(word2_4_13)

            # Word 3
            data_ID_13 = "01"
            SV_page_ID_13 = int_to_bits(page_number,6)
            availibility = bitarray(2)
            ERD1 = bitarray(14)                                      

            word3_4_13 = bitarray(0)
            word3_4_13.extend(data_ID_13)
            word3_4_13.extend(SV_page_ID_13)
            word3_4_13 += availibility + ERD1

            words4_24_13.append(word3_4_13)

            # Word 4
            ERD2 = bitarray(24)

            word4_4_13 = bitarray(0)
            word4_4_13 += ERD2

            words4_24_13.append(word4_4_13)

            # Word 5
            ERD3 = bitarray(24)

            word5_4_13 = bitarray(0)
            word5_4_13 += ERD3

            words4_24_13.append(word5_4_13)

            # Word 6
            ERD4 = bitarray(24)

            word6_4_13 = bitarray(0)
            word6_4_13 += ERD4

            words4_24_13.append(word6_4_13)

            # Word 7
            ERD4 = bitarray(24)

            word7_4_13 = bitarray(0)
            word7_4_13 += ERD4

            words4_24_13.append(word7_4_13)

            # Word 8
            ERD5 = bitarray(24)

            word8_4_13 = bitarray(0)
            word8_4_13 += ERD5

            words4_24_13.append(word8_4_13)

            # Word 9
            ERD6 = bitarray(24)

            word9_4_13 = bitarray(0)
            word9_4_13 += ERD6

            words4_24_13.append(word9_4_13)

            # Word 10
            ERD7 = bitarray(22)
            # t tilføjes i parity-funktion

            word10_4_13 = bitarray(0)
            word10_4_13 += ERD7

            words4_24_13.append(word10_4_13)

            return words4_24_13, Z_count

        # Subframe 4, reserved
        elif page_number in [14, 15, 17]:
            words4_24_res3 = []

            # Word 1
            preamble = [1,0,0,0,1,0,1,1]
            TLM = bitarray(14)                              
            ISF = bitarray([1])                                       
            reserved = bitarray(1)
            
            word1_4_res3 = bitarray(0)
            word1_4_res3.extend(preamble)                          
            word1_4_res3 += TLM                                    
            word1_4_res3.extend(ISF)
            word1_4_res3 += reserved

            words4_24_res3.append(word1_4_res3)

            # Word 2
            TOW17 = bitarray(int_to_bits(Z_count, 17))                      # First 17 bits of TOW (19 bits long in total)
            TOW18 = bitarray([0])                                           # 1: User Range Accuracy (URA) may be worse than indicated in NAV message
            TOW19 = bitarray([1])                                           # 1: Anti-spoof for the SV is turned ON
            TOW = bitarray(0)
            TOW.extend(TOW17)
            TOW.extend(TOW18)
            TOW.extend(TOW19)                 

            subframe_ID = bitarray([1, 0, 0]) 
            # t tilføjes i parity-funktion               

            word2_4_res3 = bitarray(0)
            word2_4_res3.extend(TOW)
            word2_4_res3.extend(subframe_ID)

            words4_24_res3.append(word2_4_res3)

            # Word 3
            data_ID_res3 = "01" 
            SV_page_ID_3 = int_to_bits(page_number,6)
            res22 = bitarray(16) 

            word3_4_res3 = bitarray(0)
            word3_4_res3.extend(data_ID_res3)
            word3_4_res3.extend(SV_page_ID_3)
            word3_4_res3 += res22

            words4_24_res3.append(word3_4_res3)

            # Word 4
            res23 = bitarray(24) 

            word4_4_res3 = bitarray(0)
            word4_4_res3 += res23

            words4_24_res3.append(word4_4_res3)

            # Word 5
            res24 = bitarray(24)

            word5_4_res3 = bitarray(0)
            word5_4_res3 += res24

            words4_24_res3.append(word5_4_res3)

            # Word 6
            res25 = bitarray(24)

            word6_4_res3 = bitarray(0)
            word6_4_res3 += res25

            words4_24_res3.append(word6_4_res3)

            # Word 7
            res26 = bitarray(24)

            word7_4_res3 = bitarray(0)
            word7_4_res3 += res26

            words4_24_res3.append(word7_4_res3)

            # Word 8
            res27 = bitarray(24)

            word8_4_res3 = bitarray(0)                         
            word8_4_res3 += res27

            words4_24_res3.append(word8_4_res3)

            # Word 9 OBS
            res28 = bitarray(24)

            word9_4_res3 = bitarray(0)
            word9_4_res3 += res28

            words4_24_res3.append(word9_4_res3)

            # Word 10
            res29 = bitarray(22)
            # t tilføjes i parity-funktion

            word10_4_res3 = bitarray(0)
            word10_4_res3 += res29 

            words4_24_res3.append(word10_4_res3)

            return words4_24_res3, Z_count
        
    # Subframe 5
    if subframe_number == 5: 
        if page_number <= 24:        
            words5_24 = []

            # Word 1
            preamble = [1,0,0,0,1,0,1,1]
            TLM = bitarray(14)                              
            ISF = [1]                                       
            reserved = bitarray(1)
            
            word1_5 = bitarray(0)
            word1_5.extend(preamble)                          
            word1_5 += TLM                                   
            word1_5.extend(ISF)
            word1_5 += reserved

            words5_24.append(word1_5)

            # Word 2
            TOW17 = bitarray(int_to_bits(Z_count, 17))           
            TOW18 = bitarray([0])                     
            TOW19 = bitarray([1])                    
            TOW = bitarray(0)
            TOW.extend(TOW17)
            TOW.extend(TOW18)
            TOW.extend(TOW19)               

            subframe_ID = [1, 0, 1] 
            # t tilføjes i parity-funktion                

            word2_5 = bitarray(0)
            word2_5.extend(TOW)
            word2_5.extend(subframe_ID)

            words5_24.append(word2_5)

            if SV_input_dict[SV_page_subframe5[page_number]] in tables:         # Error handling: If a satellite does not exist in the data-set

                # Word 3
                data_ID_5 = "01" 
                SV_ID_5 = int_to_bits(SV_page_subframe5[page_number],6)
                e_5 = tables[SV_input_dict[SV_page_subframe5[page_number]]]["encoded"][0]["Eccentricity"].bits[:16]

                word3_5 = bitarray(0)
                word3_5.extend(data_ID_5)
                word3_5.extend(SV_ID_5)
                word3_5.extend(e_5)

                words5_24.append(word3_5)

                # Word 4
                t_oa = tables[SV_input_dict[SV_page_subframe5[page_number]]]["encoded"][0]["TOA"].bits[:8]
                delta_i = tables[SV_input_dict[SV_page_subframe5[page_number]]]["encoded"][0]["deltai"].bits[:16]

                word4_5 = bitarray(0)
                word4_5.extend(t_oa)
                word4_5.extend(delta_i)

                words5_24.append(word4_5)

                # Word 5
                Omega_dot = tables[SV_input_dict[SV_page_subframe5[page_number]]]["encoded"][0]["OmegaDot"].bits[:16]
                SV_health = "00000000" # 8 bits

                word5_5 = bitarray(0)
                word5_5.extend(Omega_dot)
                word5_5.extend(SV_health)

                words5_24.append(word5_5)

                # Word 6
                sqrtA = tables[SV_input_dict[SV_page_subframe5[page_number]]]["encoded"][0]["sqrtA"].bits[:24]

                word6_5 = bitarray(0)
                word6_5.extend(sqrtA)

                words5_24.append(word6_5)

                # Word 7
                Omega0 = tables[SV_input_dict[SV_page_subframe5[page_number]]]["encoded"][0]["Omega0"].bits[:24]

                word7_5 = bitarray(0)
                word7_5.extend(Omega0)

                words5_24.append(word7_5)

                # Word 8
                w = tables[SV_input_dict[SV_page_subframe5[page_number]]]["encoded"][0]["omega"].bits[:24]

                word8_5 = bitarray(0)
                word8_5.extend(w)

                words5_24.append(word8_5)

                # Word 9
                M0 = tables[SV_input_dict[SV_page_subframe5[page_number]]]["encoded"][0]["M0"].bits[:24]

                word9_5= bitarray(0)
                word9_5.extend(M0)

                words5_24.append(word9_5)

                # Word 10
                af0_MSB = tables[SV_input_dict[SV_page_subframe5[page_number]]]["encoded"][0]["af0"].bits[:8]
                af1 = tables[SV_input_dict[SV_page_subframe5[page_number]]]["encoded"][0]["af1"].bits[:11]
                af0_LSB = tables[SV_input_dict[SV_page_subframe5[page_number]]]["encoded"][0]["af0"].bits[8:11]
                # t tilføjes i parity-funktion

                word10_5 = bitarray(0)
                word10_5.extend(af0_MSB)
                word10_5.extend(af1)
                word10_5.extend(af0_LSB)

                words5_24.append(word10_5)
            
                return words5_24, Z_count
            
            else:
                # Word 3
                data_ID_5 = "01" 
                SV_ID_5 = int_to_bits(SV_page_subframe5[page_number],6)
                e_5 = bitarray(16)

                word3_5 = bitarray(0)
                word3_5.extend(data_ID_5)
                word3_5.extend(SV_ID_5)
                word3_5.extend(e_5)

                words5_24.append(word3_5)

                # Word 4
                t_oa = bitarray(8)
                delta_i = bitarray(16)

                word4_5 = bitarray(0)
                word4_5.extend(t_oa)
                word4_5.extend(delta_i)

                words5_24.append(word4_5)

                # Word 5
                Omega_dot = bitarray(16)
                SV_health = "00000000" # 8 bits

                word5_5 = bitarray(0)
                word5_5.extend(Omega_dot)
                word5_5.extend(SV_health)

                words5_24.append(word5_5)

                # Word 6
                sqrtA = bitarray(24)

                word6_5 = bitarray(0)
                word6_5.extend(sqrtA)

                words5_24.append(word6_5)

                # Word 7
                Omega0 = bitarray(24)

                word7_5 = bitarray(0)
                word7_5.extend(Omega0)

                words5_24.append(word7_5)

                # Word 8
                w = bitarray(24)

                word8_5 = bitarray(0)
                word8_5.extend(w)

                words5_24.append(word8_5)

                # Word 9
                M0 = bitarray(24)

                word9_5= bitarray(0)
                word9_5.extend(M0)

                words5_24.append(word9_5)

                # Word 10
                af0_MSB = bitarray(8)
                af1 = bitarray(11)
                af0_LSB = bitarray(3)
                # t tilføjes i parity-funktion

                word10_5 = bitarray(0)
                word10_5.extend(af0_MSB)
                word10_5.extend(af1)
                word10_5.extend(af0_LSB)

                words5_24.append(word10_5)
            
                return words5_24, Z_count

        # Subframe 5, page 25
        elif page_number == 25:
            words5_24_25 = []

            # Word 1
            preamble = [1,0,0,0,1,0,1,1]
            TLM = bitarray(14)                              
            ISF = bitarray([1])                                       
            reserved = bitarray(1)
            
            word1_5_25 = bitarray(0)
            word1_5_25.extend(preamble)                          
            word1_5_25 += TLM                                    
            word1_5_25.extend(ISF)
            word1_5_25 += reserved

            words5_24_25.append(word1_5_25)

            # Word 2
            TOW17 = bitarray(int_to_bits(Z_count, 17))                      # First 17 bits of TOW (19 bits long in total)
            TOW18 = bitarray([0])                                           # 1: User Range Accuracy (URA) may be worse than indicated in NAV message
            TOW19 = bitarray([1])                                           # 1: Anti-spoof for the SV is turned ON
            TOW = bitarray(0)
            TOW.extend(TOW17)
            TOW.extend(TOW18)
            TOW.extend(TOW19)                 

            subframe_ID = bitarray([1, 0, 1]) 
            # t tilføjes i parity-funktion                

            word2_5_25 = bitarray(0)
            word2_5_25.extend(TOW)
            word2_5_25.extend(subframe_ID)

            words5_24_25.append(word2_5_25)

            # Word 3
            data_ID_5_25 = "01"
            SV_page_ID_5_25 = int_to_bits(page_number,6)
            t_oa_5 = tables[SV_input_dict[SV_page_subframe5[page_number-1]]]["encoded"][0]["TOA"].bits
            WN_a = tables[SV_input_dict[SV_page_subframe5[page_number-1]]]["encoded"][0]["WNa"].bits

            word3_5_24_25 = bitarray(0)
            word3_5_24_25.extend(data_ID_5_25)
            word3_5_24_25.extend(SV_page_ID_5_25)
            word3_5_24_25.extend(t_oa_5)
            word3_5_24_25.extend(WN_a)

            words5_24_25.append(word3_5_24_25)

            # Word 4
            SV1 = "000000"
            SV2 = "000000"
            SV3 = "000000"
            SV4 = "000000"

            word4_5_24_25 = bitarray(0)
            word4_5_24_25.extend(SV1)
            word4_5_24_25.extend(SV2)
            word4_5_24_25.extend(SV3)
            word4_5_24_25.extend(SV4)

            words5_24_25.append(word4_5_24_25)

            # Word 5
            SV5 = "000000"
            SV6 = "000000"
            SV7 = "000000"
            SV8 = "000000"

            word5_5_24_25 = bitarray(0)
            word5_5_24_25.extend(SV5)
            word5_5_24_25.extend(SV6)
            word5_5_24_25.extend(SV7)
            word5_5_24_25.extend(SV8)

            words5_24_25.append(word5_5_24_25)

            # Word 6
            SV9 = "000000"
            SV10 = "000000"
            SV11 = "000000"
            SV12 = "000000"

            word6_5_24_25 = bitarray(0)
            word6_5_24_25.extend(SV9)
            word6_5_24_25.extend(SV10)
            word6_5_24_25.extend(SV11)
            word6_5_24_25.extend(SV12)

            words5_24_25.append(word6_5_24_25)

            # Word 7
            SV13 = "000000"
            SV14 = "000000"
            SV15 = "000000"
            SV16 = "000000"

            word7_5_24_25 = bitarray(0)
            word7_5_24_25.extend(SV13)
            word7_5_24_25.extend(SV14)
            word7_5_24_25.extend(SV15)
            word7_5_24_25.extend(SV16)

            words5_24_25.append(word7_5_24_25)

            # Word 8
            SV17 = "000000"
            SV18 = "000000"
            SV19 = "000000"
            SV20 = "000000"

            word8_5_24_25 = bitarray(0)
            word8_5_24_25.extend(SV17)
            word8_5_24_25.extend(SV18)
            word8_5_24_25.extend(SV19)
            word8_5_24_25.extend(SV20)

            words5_24_25.append(word8_5_24_25)

            # Word 9
            SV21 = "000000"
            SV22 = "000000"
            SV23 = "000000"
            SV24 = "000000"

            word9_5_24_25 = bitarray(0)
            word9_5_24_25.extend(SV21)
            word9_5_24_25.extend(SV22)
            word9_5_24_25.extend(SV23)
            word9_5_24_25.extend(SV24)

            words5_24_25.append(word9_5_24_25)

            # Word 10
            res30 = bitarray(6)
            res31 = bitarray(16)
           # t tilføjes i parity-funktion

            word10_5_24_25 = bitarray(0)
            word10_5_24_25 += res30 + res31

            words5_24_25.append(word10_5_24_25)

            return words5_24_25, Z_count


subframe(2, 0, 1, Z_count_start)

def frame(SV,page_number,z_count):
    oneframe=[]
    for i in range(3):
        oneframe.append(subframe(i+1,0,SV,z_count))
        z_count += 1

    oneframe.append(subframe(4,page_number,SV,z_count))
    z_count += 1

    oneframe.append(subframe(5,page_number,SV,z_count))
    z_count += 1
    return oneframe, z_count

frame(1,1,Z_count_start)

def framelist(SV,z_count):
    frame25=[]
    for i in range(25):
        f=frame(SV,i+1,z_count)
        frame25.append(f[0])
        z_count=f[1]
    return frame25,z_count

def frames(SV: int, Z_count: int):
    frame25 = bitarray(0)
    Z_countinc = Z_count
                                                                                     # Frame 1-25    
    frame25,Z_countinc=append_parity(framelist(SV,Z_countinc))
        
    return frame25

(frames(1, Z_count_start))

buddinge=55.738957, 12.500242, 20

def modulo2_frames_runs(SV, Z_count, PRN):
    padding=bitarray()#(paddelay(SV,buddinge)*"0")
    ca = ca_code(PRN).copy()
    CA_original = ca * 20
    CA_inverted = (~ca) * 20            # precompute PRN codes, original and inv


    flags = bitarray(frames(SV, Z_count))            # bitarray

    assert len(CA_original) == 20460
    assert len(CA_inverted) == 20460
    assert len(flags) > 0

    n = len(flags)
    block_len = len(CA_original)
    out = bitarray(block_len * n)       # build bit array to avoid pc doing "oops bit array needs more memory" delays


    # Find indices where the bit flips, as opposed to before where it checked every bit
    t01 = list(flags.search(bitarray('01')))
    t10 = list(flags.search(bitarray('10')))    #search is written in C, we like that
    transitions = sorted(t01 + t10)             # this is a list of where to flip in the 37500 long bitarray


    # Run boundaries
    boundaries = [0] + [i + 1 for i in transitions] + [n]   #turns transistions into actual locations


    pos = 0
    for a, b in zip(boundaries, boundaries[1:]):    # pairs a,b
        run_len = b - a                                     #finds lenght between a and b
        blk = CA_inverted if flags[a] else CA_original      #inserts wheather 1 or 0
        out[pos:pos + run_len * block_len] = blk * run_len  #creates block length and slices it into the premade out
        pos += run_len * block_len                          #updates position


    return padding+out

res = modulo2_frames_runs(1,Z_count_start,1)
