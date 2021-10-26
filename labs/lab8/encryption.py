"""
William McClain
encryption.py
Problem: These are functions for encoding to be imported into lab8.py
Affirmation: I affirm that everything in this code is my own work with the help of the TA and LT
"""


def encode(text_in, key):
    text_list = []
    key_in = key
    text_list[:0] = text_in
    i = 0
    encode_txt = ''
    for val in text_list:
        num = ord(val)
        num = num + key_in
        # these two if statements take the loop of the alphabet into account and if spaces are in the text
        if num > 122:
            num = num - 26
        if num == key_in + 32:
            num = 32
        new_ch = chr(num)
        text_list[i] = new_ch
        print(text_list[i], end='')
        i = i + 1
        encode_txt = encode_txt + new_ch
    return encode_txt


def encode_better(text_in, key_in):
    text_in.lower()
    text_list = []
    key_in.lower()
    text_list[:0] = text_in
    key_list = []
    key_list[:0] = key_in
    i = 0
    n = len(key_list)

    for val in text_list:
        num = ord(val)
        knum = ord(key_list[((i + n) % n)])
        num_shift = knum - 97
        num = num + num_shift
        new_ch = chr(num)
        text_list[i] = new_ch
        print(text_list[i], end='')
        i = i + 1