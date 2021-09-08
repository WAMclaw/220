"""
William McClain
interest.py
Problem: Create a code that calculates the monthly interest of a User
I affirm that the contents of this code are my completely my own creation.
"""

def main():
    #Asking for user input and assigning variables to each
    rate = eval(input("Please input the annual interest rate here: "))
    days = eval(input("Please input the number of days in this billing cycle here: "))
    previous_balance = eval(input("Please give the previous balance on the card here: $"))
    pay = eval(input("Please give the amount of payment here: $"))
    pay_day = eval(input("Please give the day this payment was made here: "))
    #Calculating daily balance
    #daily_balance = ((previousBalance*days)-(payment*(days-paymentDay)))/days
    #calculating monthly interest rate
    #monthly_rate = rate/(12*100)
    #calculating monthly interest
    #interest = round(daily_balance*monthly_rate,2)
    interest = round((((previous_balance*days)-(pay*(days-pay_day)))/days)*(rate/(12*100)),2)
    #print("The monthly interest rate of the card is $",interest)
    #above line taken out because the tests did not like all the fluff
    print(interest)

if __name__ == '__main__':
    main()
