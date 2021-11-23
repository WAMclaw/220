from algorithms import read_data, is_in_linear
from random import randint
"""
Name: William McClain
lab12.py
Problem: use while loops to create a funciton that finds and replaces a value in a list with my name,
imports a txt file and creates a list out of the lines data and searches if a value is in the list,
forces a user to input an integer variable between 1-10, counts the digits of a number, and a function
that creates a guessing number game with 7 guesses and 1-100 range of secret number.
Affirmation: I affirm that this is all my own work
"""


# def read_data(file_name):
#     num_file = open(file_name, 'r')
#     numbs = []
#     i = 0
#     while i < len(file_name):  # for line in num_file:
#         line = num_file.readline()
#         # line.strip('\n')
#         num = line.split()
#         print(num)
#         c = 0
#         while c < len(num):
#             numbs.append(float(num[c]))
#             c += 1
#         i += 1
#     num_file.close()
#     return numbs
#
#
# def is_in_linear(search_value, values):
#     return search_value in values


def find_and_remove_first(a_list, value):
    ind_val = a_list.index(value)
    a_list.pop(ind_val)
    a_list.insert(ind_val, 'Will')


def good_input():
    user_in = float(input('Please Give a number between 1 and 10: '))
    while user_in not in range(1,10):
        print('The number given was outside of the range 1-10.')
        user_in = float(input('Please give a number between 1 and 10: '))
    return user_in


def num_digits():
    user_in = eval(input('Give a positive integer to find the number of digits: '))
    while user_in > 0:
        c = 0
        while user_in > 0:
            user_in = user_in//10
            c += 1
        print('The number of digits is', c)
        print('Enter 0 or a negative number to exit or')
        user_in = eval(input('Give a positive integer to find the number of digits:'))


def hi_lo_game():
    s_number = randint(1, 100)
    print("Let's play a game!")
    print("Guess the secret number between 1-100.")
    print("I'll tell you whether you're high or low or if you guess it!")
    print("Let's Begin. Give me a guess!")
    user_guess = eval(input())
    c = 1
    while c < 7:
        if user_guess > s_number:
            print("To High! Guess again!")
            c += 1
            user_guess = eval(input())
        if user_guess < s_number:
            print("To Low! Guess again!")
            c += 1
            user_guess = eval(input())
        else:
            print("You Got IT! Game Over!")
            win_c = c
            print("You WON in", win_c, "guesses!")
            c = 8
        if c == 7:
            print("Sorry. You lost. The number was", s_number, ".")


def main():
    # dumb = [1, 4, 5, 3, 8, 9]
    # find_and_remove_first(dumb,3)
    # num_list = read_data('dataSorted.txt')
    # print(num_list)
    # ans = is_in_linear(13, num_list)
    # print(ans)
    # good_input()
    # num_digits()
    # hi_lo_game()
    pass


if __name__ == '__main__':
    main()
