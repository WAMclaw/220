"""
Name: William McClain
lab9.py
Problem: for addTens get a list of numbers and add 10 to each, squareEach is similar but square each number,
    sumlist take the list and give a sum of the numbers, toNumbers takes a list of strings and makes them
    into a list of ints, writeSumOfSquares takes the previous three fncs and uses them to read a file
    and output to a different file the sum of squares of each line, starter uses logic statements to
    see if a wrestler can start based on conditions, leapYear sees if a year is a leap year based on
    conditions, circleOverlap sees if a circle drawn in a graphics window overlaps a hardcoded cirle in
    the window
Affirmation: I affirm that the code below is all my own work with help from the TA and LT.
"""
from graphics import Circle, Point, GraphWin, Text


def addTens(nums):
    numl = []
    numl[:] = nums
    for num in range(len(numl)):
        numl[num] = numl[num] + 10
        nums[num] = numl[num]


def squareEach(nums):
    numl = []
    numl[:] = nums
    for num in range(len(numl)):
        numl[num] = numl[num] ** 2
        nums[num] = numl[num]


def sumlist(nums):
    num_sum = 0
    for num in nums:
        num_sum = num_sum + num
    return num_sum

def toNumbers(strList):
    numl = []
    numl[:] = strList
    for num in range(len(numl)):
        numl[num] = eval(numl[num])
        strList[num] = numl[num]


def squareEachAlpha(nums):
    numl = []
    numl[:] = nums
    for num in range(len(numl)):
        numl[num] = numl[num] ** 2
        nums[num] = numl[num]
    return numl


def toNumbersAlpha(strList):
    numl = []
    numl[:] = strList
    for num in range(len(numl)):
        numl[num] = eval(numl[num])
        strList[num] = numl[num]
    return strList


def writeSumOfSquares():
    file_in = input('Give a file [file.txt] containing at least two numbers\n'
                    'per line to be squared and have their sums given: ')
    txt_in = open(file_in, 'r')
    txt_out = open('sum_out.txt', 'w')
    for line in txt_in:
        lista = line.rsplit()
        sum_o_sqs = sumlist(squareEachAlpha(toNumbersAlpha(lista)))
        txt_sum = 'Sum of Squares = ' + str(sum_o_sqs) + '\n'
        txt_out.write(txt_sum)

def beta_writeSumOfSquares():
    file_in = input('Give a file [file.txt] containing at least two numbers\n'
                    'per line to be squared and have their sums given: ')
    txt_in = open(file_in, 'r')
    txt_out = open('sum_out.txt', 'w')
    for line in txt_in:
        lista = line.rsplit()
        # sumlist(squareEachAlpha(toNumbersAlpha(lista)))
        txt_sum = 'Sum of Squares = ' + str(sumlist(squareEachAlpha(toNumbersAlpha(lista)))) + '\n'
        txt_out.write(txt_sum)

def starter():
    weight = eval(input('Enter the wrestlers weight: '))
    num_wins = eval(input('Enter the wrestlers number of wins: '))
    if weight >= 150 or weight < 160 and num_wins >= 5:
        print('They can start.')
    elif weight > 199 or num_wins > 20:
        print('They can start.')
    else:
        print('They cannot start.')


def leapYear(year):
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False


def circleOverlap():
    circ_win_h = 500
    circ_win_w = 500

    win_circ = GraphWin("Circle", circ_win_w, circ_win_h)
    circ_text_pt = Point(circ_win_w / 2, circ_win_h - 70)
    circ_text_pt2 = Point(circ_win_w / 2, circ_win_h - 50)

    circ_inst = Text(circ_text_pt, "Choose two points for your circle, the first being the center point.")
    circ_inst.draw(win_circ)
    circ_inst2 = Text(circ_text_pt2, "The second point will be a point on the circumference.")
    circ_inst2.draw(win_circ)

    circ_c1 = win_circ.getMouse()
    circ_c1.draw(win_circ)
    circ_c2 = win_circ.getMouse()
    circ_c2.draw(win_circ)

    chp = Point(150, 150)
    circ_hard = Circle(chp, 100)
    circ_hard.draw(win_circ)

    # calculate radius
    # user circle
    circ_dif_x1 = abs(circ_c1.getX() - circ_c2.getX())
    circ_dif_y1 = abs(circ_c1.getY() - circ_c2.getY())
    circ_radius1 = ((circ_dif_x1 ** 2) + (circ_dif_y1 ** 2)) ** (1 / 2)
    circ = Circle(circ_c1, circ_radius1)
    circ.draw(win_circ)
    circ_center1 = circ.getCenter()

    chp = Point(150, 150)
    circ_hard = Circle(chp, 100)
    circ_hard_rad = 100
    circ_hard.draw(win_circ)
    circ_dif_x = abs(chp.getX() - circ_center1.getX())
    circ_dif_y = abs(chp.getY() - circ_center1.getY())
    dist_centers = ((circ_dif_x ** 2) + (circ_dif_y ** 2)) ** (1 / 2)

    # click for close
    circ_inst.setText("Click again to quit")
    circ_inst2.setText("")

    rad_text_pt = Point(circ_win_w / 2, circ_win_h - 30)
    if dist_centers >= (circ_radius1 + circ_hard_rad):
        rad = "The circles do not overlap."
    else:
        rad = 'The circles overlap!'
    circ_rad_fin = Text(rad_text_pt, rad)
    circ_rad_fin.draw(win_circ)

    win_circ.getMouse()
    win_circ.close()


def main():
    # list = [1, 2, 3, 4, 5]
    # strList = ['1', '2', '3.0', '4.2', '5.5']
    # year = 2001
    # print(strList)
    # print(list)
    # addTens(list)
    # squareEach(list)
    # print(sumlist(list))
    # toNumbers(strList)
    # writeSumOfSquares()
    beta_writeSumOfSquares()
    # starter()
    # leapYear(year)
    # circleOverlap()
    # print(list)
    # print(strList)
    pass


main()
