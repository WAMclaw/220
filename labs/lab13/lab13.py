"""
Name: William McClain
lab13.py
Problem:
Affirmation: I affirm this is all my own work with help from the TA and LT.
"""


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


def star_find(values):
    sig_count = 0
    sig_ind = []
    sig_ord = []
    # if you want to make it stop at the fifth use the following while loop and fix bottom of function
    # while sig_count < 5: # run through the code below afterwards and add a break if code hits end of list
    for item in values:
        if 4000 <= item <= 5000:
            sig_ind.append(values.index(item))
            sig_ord.append(item)
            sig_count += 1
        else:
            pass
    if sig_count >= 5:
        print("You've found a Neutron star!")
        print("You found", len(sig_ord), "signals. Seen below.")
        print(sig_ord)
        print("You had to go through", sig_ind[4], "many other signals before reaching a 5th!")
    else:
        print("You've not found a Neutron star. Keep Trying!")


def main():
    new_signals = read_data('signals.txt')
    star_find(new_signals)
    # add other function calls here
    pass


main()
