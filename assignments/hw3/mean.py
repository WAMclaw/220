"""
William McClain
mean

Problem: program needs to calculate the root mean square average, the harmonic mean
and the geometric mean of a user input set of variables
The user must be ble to specify the amount of numbers input
"""
import math

def main():

    # spell out code
    #print("This code will calculate the root mean square average,")
    #print("the harmonic mean and the geometric mean of a string of numbers.")
    #print()
    # user input of amount of numbers (n)
    amount = eval(input("Please give the amount of numbers you will be inputting: "))
    print()
    # user input of numbers through loops
    x_array = [1] * amount
    # still need a way for them to input the values with a loop
    for i in range(amount):
        xus = "Input value " + str(i+1) + " :"
        x_array[i] = eval(input(xus))
    print()
    # print(x_array) #testing to see if array
    # could add something to sort the array and correct fo user error
    # x_values_sorted = sort(x_values) #taken out for troubleshooting
    # calculate rms average sum by loops
    num_nfrms = 0
    for irms in x_array:
        num_nfrms = num_nfrms + (irms ** 2)
    # calculate rms average in outside equation
    rms_average = round(math.sqrt(num_nfrms / amount), 3)
    # calculate harmonic mean sum by loops
    num_nharmonic = 0
    for harm in x_array:
        num_nharmonic = num_nharmonic + (1/harm)
    # calulate harmonic mean by outside equation
    harmonic_mean = round(amount / num_nharmonic, 3)
    # calculate geometric mean sum by loops
    num_ngeometric = 1
    for geom in x_array:
        num_ngeometric = num_ngeometric * geom
    # calculate geometric mean by outside equation
    geometric_mean = round(math.pow(num_ngeometric, (1/amount)), 3)
    # print outputs
    print(rms_average)
    print(harmonic_mean)
    print(geometric_mean)


if __name__ == '__main__':
    main()
