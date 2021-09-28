"""
William McClain
traffic.py

Problem: Take a number of roads surveyed, the number of days each road was individually surveyed, and
calculate the average vehicles per day. Then it should give the average vehicles per day on all roads
and the average number of vehicles per road.

Affirmation: I affirm that all of the code below is my own work.
"""


def main():
    # input for the amount of roads, place holder number and place holder array
    road_amount = eval(input("Give the number of roads surveyed: "))
    road_number = 0
    total_cars = 0
    # big_array = [0] * road_amount

    for i1 in range(road_amount):
        # first loop gets input of days each road was monitored
        # makes an array within big_array for the input given in the later loop
        road_number = road_number + 1
        road_num_txt = str(road_number)
        road_day_txt = "How many days was road " + road_num_txt + " surveyed:"
        road_day_input = eval(input(road_day_txt))
        road_day = 0
        per_road_total = 0
        # small_array = [0] * road_day_input
        # big_array[num_road - 1] = small_array
        for i2 in range(road_day_input):
            # creates a loop for the inputs of the amount of cars per day on a given road
            # places the input in the designated spot with in each array
            road_day = road_day + 1
            day_txt = str(road_day)
            car_amount_txt = "How many cars were on road " + road_num_txt + " on Day " + day_txt + ": "
            car_amount_input = eval(input(car_amount_txt))
            per_road_total = per_road_total + car_amount_input

            total_cars = total_cars + car_amount_input
            # small_array[day_road - 1] = car_amount_input
        # test to see if add properlly
        prt_num = str(per_road_total)
        prt_txt = "The total cars for Day " + day_txt + " is " + prt_num
        print(prt_txt)

    # prints final total and average
    total_cars_num = str(total_cars)
    total_cars_txt = "The total number of cars: " + total_cars_num
    print(total_cars_txt)


if __name__ == '__main__':
    main()
