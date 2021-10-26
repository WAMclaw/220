"""
Name: William McClain
Partner: NA
lab7.py
Affirmation: I affirm that this code is all my wn work with help from the TA and LT.
Problem: create a function for taking an integer and putting in in dollar and cent format
1 create a function that puts a message through a Caesar cipher
2 create a function to take an argument and calculate the area of a sphere
3 create a function as above but for the volume of a sphere
4 create a function to take an argument and calculate the sum of natural numbers
5 create a function as above but for the cubes of natural numbers
6 create a function to put a message through the Vigenere cipher
"""
from math import pi

def cash_conversion():
    user_in = eval(input('Enter an Integer to be turned into a cash amount:'))
    print('{:.2f}'.format(user_in))


def encode():
    text_in = input('Enter a message to be encoded through a Caesar cipher: ')
    text_in.lower()
    text_list = []
    key_in = eval(input('Enter a number as the key for the cipher: '))
    text_list[:0] = text_in
    i = 0
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


def sphere_area(radius):
    area = 4 * pi * radius ** 2
    return print('{:.4f}'.format(area))


def sphere_volume(radius):
    volume = (4 / 3) * pi * radius ** 3
    return print('{:.4f}'.format(volume))


def sum_n(n):
    sumn = (n * (n + 1)) / 2
    return print('{:.3f}'.format(sumn))


def sum_n_cubes(n):
    sumcube = ((n ** 2) * ((n + 1) ** 2)) / 4
    return print('{:.3f}'.format(sumcube))


def encode_better():
    text_in = input('Enter a message to be encoded through a Vigenere cipher: ')
    text_in.lower()
    text_list = []
    key_in = input('Enter a word/series of letter as the key for the cipher: ')
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


def main():
    # add function calls here
    # cash_conversion()
    # encode()
    # sphere_area(3)  # should give area of 113.0973
    # sphere_volume(3)  # should give volume of 113.0973
    # sum_n(35)  # should give sum of 630
    # sum_n_cubes(35)  # should give sum of 396900
    encode_better()

    pass


main()
