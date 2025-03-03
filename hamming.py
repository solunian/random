# https://www.youtube.com/watch?v=b3NxrZOu_CE
# shockingly simple on hardware, the indicating parity bits give the location for the wrong bit. if only one error.

# 1st parity bit: all bits with ___1
# 2nd parity bit: all bits with __1_
# 3rd parity bit: all bits with _1__
# 4th parity bit: all bits with 1___

# algo for the parity bits: xor all the positions of data with a 1 bit. resulting bitstring gives the parity bits.

import numpy as np
from functools import reduce

# technically would just be 11 bits. but just pretend that the 1, 2, 4, 8 spots are all 0 at the beginning.
# after finding the parity, they will all be set to the correct parity value.
bits = np.random.randint(0, 2, 16)
parity_bitstr = reduce(
    lambda x, y: x ^ y, [i for i, bit in list(enumerate(bits)) if bit]
)

print("=== RANDOM 16 BITS ===")
for i in range(0, 16, 4):
    print(bits[i : i + 4])

print(f"\nparity bitstr: {bin(parity_bitstr)}")

for i in range(0, 4):
    bits[2**i] = parity_bitstr % 2
    parity_bitstr /= 2

bits[0] = len([bit for bit in bits if bit == 1]) % 2

print(f"0th bit: {bits[0]}\n")

print("=== EXTENDED HAMMING CODE WITH 16 BITS ===")
for i in range(0, 16, 4):
    print(bits[i : i + 4])
