"""
Name: William McClain
lab3.py
I affirm that this program is all my own work, with help from the TA and LT.
"""
import math
#average() - create an averaging function
def average():
    amount_grades = eval(input("Please give the number of grades: "))
    grade_sum = 0
    for i in range(amount_grades):
        print("Enter your grade on HW",i+1,end=":")
        grade_in = eval(input(""))
        grade_sum = grade_sum+grade_in
    grade_average = round(grade_sum/amount_grades)
    print("The average of your grades is:", round(grade_average,2))

#tip_jar() - create an adding function for 5 users and 5 inputs
def tip_jar():
    tipping = 5
    tips = 0
    for i in range(1,tipping+1):
        print("Enter your donation amount: $0.00",end="")
        ph_tip = eval(input(""))
        tips = tips+ph_tip
        print("Please pass to the next person")
        print()
    print("Your total is: $",round(tips,3))

#takes the input of a number and approximate and inputs them into a function to
#approximate the square root of the number
def newton():
    print("This code will use Sir Issac Newton's method to approximate a square root.")
    new_number = eval(input("Give a number:"))
    approx = eval(input("Give a number of approximations"))
    approx = (approx + (new_number/approx))/2
    print("The number: ",new_number)
    print("The approximate square root: ", approx)

# create a function that prints a sequence following the 1,3,3,5,5,7,7,... pattern
def sequence():
    sequence_number = eval(input("Give a number for the amount of numbers in a series"))
    alternate_val = 1
    for i in range(1,sequence_number+1):
        print(alternate_val,end="\t")
        alternate_val = alternate_val + (i%2)*2

#create a function that approximates pi after user input for n terms
def pi():
    term_amount = eval(input("Give [n] number of terms in the series: "))
    term_numerator = 1
    alternate_val_pi = 1
    #pi_act = math.pi/2 #just checking value of pi/2
    #print(pi_value)
    pi_value = 1
    for i in range(term_amount):
        term_numerator = alternate_val_pi + 1
        alternate_val_pi = alternate_val_pi + (i%2)*2
        #print(term_numerator)
        #print(alternate_val_pi)
        pi_value = pi_value * (term_numerator/alternate_val_pi)
        #print(pi_value)
    pi_value=pi_value*2
    print(pi_value)