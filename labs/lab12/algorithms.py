"""
William McClain
algorithms.py
Problem: create functions that imports a txt file and creates a list out
of the lines data and searches if a value is in the list
Affirmation: I affirm that this is all my own work
"""


def read_data(file_name):
    num_file = open(file_name, 'r')
    numbs = []
    i = 0
    while i < len(file_name):  # for line in num_file:
        line = num_file.readline()
        # line.strip('\n')
        num = line.split()
        print(num)
        c = 0
        while c < len(num):
            numbs.append(float(num[c]))
            c += 1
        i += 1
    num_file.close()
    return numbs


def is_in_linear(search_value, values):
    return search_value in values
