"""
Name: William McClain
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    lengthv = eval(input("Enter the length: "))
    widthv = eval(input("Enter the Length: "))
    heightv = eval(input("Enter the height: "))
    volume = lengthv * widthv * heightv
    print("Volume =", volume)


def shooting_percentage():
    totshots = eval(input("Enter the total shots: "))
    madeshots = eval(input("Enter the shots made: "))
    percshot = madeshots / totshots
    print("Your shot percentage is [",percshot,"]")


def coffee():
    lbscoff = eval(input("Enter the amount [in pounds] of coffee you would like to order: "))
    shplb = 0.86
    coffplb = 10.50
    fixcofst = 1.50
    coffcost = lbscoff * (shplb + coffplb) + fixcofst
    print("Your coffee cost total is [$",coffcost,"]")

def kilometers_to_miles():
    mtok = 1/1.61
    kiloms = eval(input("Enter the number of kilometers of travel: "))
    miles = mtok * kiloms
    print("The number miles you'll travel is [",miles,"]")