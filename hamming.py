# https://www.youtube.com/watch?v=b3NxrZOu_CE
# shockingly simple on hardware, the indicating parity bits give the location for the wrong bit. if only one error.

# 1st parity bit: all bits with ___1
# 2nd parity bit: all bits with __1_
# 3rd parity bit: all bits with _1__
# 4th parity bit: all bits with 1___

# algo for the parity bits: xor all the positions of data with a 1 bit. resulting bitstring gives the parity bits.

import math
import numpy as np
from functools import reduce

# technically would just be 11 bits. but just pretend that the 1, 2, 4, 8 spots are all 0 at the beginning.
# after finding the parity, they will all be set to the correct parity value.

power = 6  # even power makes printing look better
chunk_size = 2**power

# prep chunk.
bits = np.random.randint(0, 2, chunk_size)
# clean out the parity bit spots into 0. 0, and all powers of 2
bits[0] = 0
for i in range(power):
    bits[2**i] = 0


def print_bits():
    space = math.ceil(chunk_size**0.5)  # fit a close to square size
    for i in range(space):
        print(bits[i * space : i * space + space])


parity_bitstr = reduce(
    lambda x, y: x ^ y, [i for i, bit in list(enumerate(bits)) if bit]
)

print("=== RANDOM BITS ===")
print_bits()

print(f"\nparity bitstr: {bin(parity_bitstr)}")

for i in range(0, power):
    bits[2**i] = parity_bitstr % 2
    parity_bitstr /= 2

bits[0] = len([bit for bit in bits if bit == 1]) % 2

print(f"0th bit: {bits[0]}\n")

print(
    f"=== EXTENDED HAMMING CODE ({chunk_size - power - 1} DATA, {power + 1} PARITY) ==="
)
print_bits()
