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
        # strips the line and puts it into a string
        b_line = line.rstrip('\n')
        list_alpha = b_line.split(':')
        # print(list_alpha) # test for alpha list
        list_beta = list_alpha[1]
        # print(list_beta) # test for beta list
        list_in = list_beta.split()
        # print(list_in) # tests the list
        n = int((len(list_in)) / 2)
        # print(n) # test for length to make sure it's not a float
        weight_total = 0
        total = 0
        for v in range(n):
            weight_total = weight_total + int(list_in[v * 2])
        # print(weight_total) # test for weight total per student should = 100
        if weight_total == 100:
            for i in range(n):
                mul = int(list_in[i * 2]) * int(list_in[i * 2 + 1])
                total = total + mul
            # print(mul)
            # print(total)
            w_avg = round(total / 100, 1)
            w_avg_str = str(w_avg)
            all_grade_total = all_grade_total + w_avg
            n_students = n_students + 1
        elif weight_total > 100:
            w_avg_str = 'Error: The weights are more than 100.'
        else:
            w_avg_str = 'Error: The weights are less than 100.'
        # print(w_avg) # test for weighted average per student
        str_out = list_alpha[0] + "'s average: " + w_avg_str + '\n'
        print(str_out) # test for output text
        # print(all_grade_total) # test for total of all grades
        txt_out.write(str_out)
    class_average = all_grade_total / n_students
    print(class_average)


def main():
    weighted_average('grades.txt', 'avg.txt')


if __name__ == '__main__':
    main()
