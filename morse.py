#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
__author__ = 'Shanquel Scott working in group with Gaby, Sondos'
# and study hall worked with John and Piero'

import re
from morse_dict import MORSE_2_ASCII


def decode_bits(bits):
    bits = bits.strip('0')
    sorting_nums = min([len(g) for g in re.findall(r"1+|0+", bits)])
    bits_to_morse = bits.replace('0000000' * sorting_nums, '   ')
    bits_to_morse = bits_to_morse.replace('000' * sorting_nums, ' ')
    bits_to_morse = bits_to_morse.replace('111' * sorting_nums, '-')
    bits_to_morse = bits_to_morse.replace('1' * sorting_nums, '.')
    bits_to_morse = bits_to_morse.replace('0' * sorting_nums, '')
    bits_to_morse = bits_to_morse.replace('0', '')
    return bits_to_morse


def decode_morse(morse):
    str1 = ''
    for word in morse.strip().split("   "):
        for char in word.strip().split(" "):
            str1 += MORSE_2_ASCII[char]
        str1 += " "
    return str1.strip()


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "11001100110011000000110000001111110011001111110011111100000000000000000000011001111110011111100111111000000110011001111110000001111110011001100000011" # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")
    print("\nCompleted.")
