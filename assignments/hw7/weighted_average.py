"""
William McClain
weighted_average.py
Problem: create a code that reads names and corresponding grades from a txt file into the code and
calculates the weighted average of the grades and writes the average to a separate txt file.
Affirmation: I affirm that all of the code below is my own work.
"""


def weighted_average(in_file_name, out_file_name):
    # opens inputs and outputs
    txt_in = open(in_file_name, 'r')
    txt_out = open(out_file_name, 'w')
    # sets out trackers and class grade total
    all_grade_total = 0
    n_students = 0
    # loop that goes through each txt file line
    for line in txt_in:
        b_line = line.rstrip('\n')  # strips the line and puts it into a string
        list_alpha = b_line.split(':')  # creates list of 2 items, name and numbers
        list_numbers = list_alpha[1]  # takes the numbers into a new string
        list_in = list_numbers.split()  # put the numbers into a list
        n = int((len(list_in)) / 2)
        weight_total = 0
        total = 0
        for v in range(n):
            weight_total = weight_total + int(list_in[v * 2])
        if weight_total == 100:  # if, elif, and else statements to separate data
            for i in range(n):  # multiplies the weight and grade and the ads the product to a total
                mul = int(list_in[i * 2]) * int(list_in[i * 2 + 1])
                total = total + mul
            w_avg = round(total / 100, 1)  # finds the weighted average per student
            w_avg_str = str(w_avg)
            all_grade_total = all_grade_total + w_avg  # only adds totals that are weighted properly
            n_students = n_students + 1
        elif weight_total > 100:
            w_avg_str = 'Error: The weights are more than 100.'
        else:
            w_avg_str = 'Error: The weights are less than 100.'
        str_out = list_alpha[0] + "'s average: " + w_avg_str + '\n'
        txt_out.write(str_out)

    class_average = round(all_grade_total / n_students, 1)
    final_str_out = 'Class average: ' + str(class_average)
    txt_out.write(final_str_out)
    txt_out.close()


def main():
    weighted_average('grades.txt', 'avg.txt')


if __name__ == '__main__':
    main()
