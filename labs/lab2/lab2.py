"""
Name: William McClain
lab2.py
Problem: create function that creates the sum of threes chosen by a user, create a function that makes a multiplication table
create a function that adds squareroots of user inputs, create a function that manually calculates a square
"""
import math


def sum_of_threes():
    bound_sot = eval(input("Please give an upper bound: "))
    variable_of_three = 0
    for in_three in range(3,bound_sot+1,3):
        variable_of_three = variable_of_three + in_three
    print("The sum of the threes is ", variable_of_three)



def multiplication_table():
    multab = 1

    for i in range(1,11):
        for x in range(multab,multab*10+1,multab):
            print(x, end=" ")



def triangle_area():
    sidea = eval(input("Please input the first side: "))
    sideb = eval(input("Please input the second side: "))
    sidec = eval(input("Please input the third side: "))

    S = (sidea+sideb+sidec)/2
    Area = math.sqrt(S*(S-sidea)*(S-sideb)*(S-sidec))
    print("The area of the triangle is [",Area,"] units squared.")

def sumSquares():
    lowerb = eval(input("Enter a lower bound:"))
    upperb = eval(input("Enter an upper bound: "))
    pwr = 0
    for add in range(lowerb,upperb+1):
        pwr = add ** 2
        #print(pwr)

        #print(pwrsum)

    print("The sum of your squares is ",pwr)



def power():
    basep = eval(input("Enter a base: "))
    pwrp = eval(input("Enter an exponent: "))
    for tim in range(pwrp):
        fin = basep*basep
print(basep," ^ ",pwrp," = ",fin)
