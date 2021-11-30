"""
William McClain
algorithms.py
Problem: create functions that imports a txt file and creates a list out
of the lines data and searches if a value is in the list
Affirmation: I affirm that this is all my own work
"""
from graphics import Rectangle, Point


def read_data(file_name):
    num_file = open(file_name, 'r')
    line_amount = num_file.readlines()
    i = 0
    numbs = []
    while i < len(line_amount):  # for line in num_file:
        line = line_amount[i]
        # line.strip('\n')
        num = line.split()
        # print(num)
        c = 0
        while c < len(num):
            numbs.append(float(num[c]))
            c += 1
        i += 1
    num_file.close()
    return numbs


def is_in_linear(search_value, values):
    return search_value in values


def is_in_binary(search_value, values):
    left_lop = 0
    right_lop = len(values) - 1

    while left_lop <= right_lop:
        middle_lop = (left_lop + right_lop) // 2
        if search_value == values[middle_lop]:
            return True
        if search_value < values[middle_lop]:
            right_lop = middle_lop - 1
        if search_value > values[middle_lop]:
            left_lop = middle_lop + 1
    return False


# def selection_sort(values):
#     unsort_index = 0
#     new = []
#     for item in range(len(values)):
#         new.append(values.pop(values.index(min(values))))
#     # values.pop(values.index(min(values)))
#     print(new)
#
#     for item in range(len(values) - 1):
#         mini = item
#         for new in range(item + 1, len(values)):
#             if values[new] < values[mini]:
#                 mini = new
#         tem =


def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    diff_x = abs(p1.getX() - p2.getX())
    diff_y = abs(p1.getY() - p2.getY())
    return diff_x * diff_y


def main():
    selection_sort([2,4,3,1])

if __name__ == "__main__":
    main()