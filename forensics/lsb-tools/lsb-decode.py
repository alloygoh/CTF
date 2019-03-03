#!/usr/bin/env python3

from bitstring import BitStream, BitArray

file = "pico2018-special-logo.bmp"
header = 14*8

b = BitArray(bytes=open(file, 'rb').read())
nb = b.bin[header:]

bin_char = ''
count = 0
while len(nb) > 0:
    byte, nb = nb[:8], nb[8:]
    bin_char += byte[-1]
    count += 1
    if len(bin_char) == 8:
        print(chr(int(bin_char, 2)), end='')
        bin_char = ''
    if count > 2000:
        break

