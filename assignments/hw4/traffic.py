"""
William McClain
traffic.py

Problem: Take a number of roads surveyed, the number of days
each road was individually surveyed, and
calculate the average vehicles per day. Then it should give
the average vehicles per day on all roads
and the average number of vehicles per road.

Affirmation: I affirm that all of the code below is my own work.
"""


def main():
    # input for the amount of roads, place holder number and place holder array
    road_amount = eval(input("Give the number of roads surveyed: "))
    road_number = 0
    total_cars = 0

    for _ in range(road_amount):
        # first loop gets input of days each road was monitored
        road_number = road_number + 1
        road_day_txt = "How many days was road " + str(road_number) + " surveyed:"
        road_day_amount = eval(input(road_day_txt))
        road_day = 0
        per_road_total = 0
        for _ in range(road_day_amount):
            # creates a loop for the inputs of the amount of cars per day
            # on a given road
            road_day = road_day + 1
            car_amount_txt = "How many cars were on road " + str(road_number) \
                             + " on Day " + str(road_day) + ": "
            car_amount_input = eval(input(car_amount_txt))
            per_road_total = per_road_total + car_amount_input
            total_cars = total_cars + car_amount_input
        # prints average cars per day on a given road
        avg_per_road = per_road_total/road_day_amount
        prt_average_txt = "Average vehicles per day of Road " \
                          + str(road_number) + ": " + str(round(avg_per_road, 2))
        print(prt_average_txt)

    # calculate and print final total and average
    total_cars_txt = "Total number of cars: " + str(round(total_cars, 2))
    total_average = total_cars/road_amount
    total_avg_txt = "Average number of cars per road: " + str(round(total_average, 2))

    print(total_cars_txt)
    print(total_avg_txt)


if __name__ == '__main__':
    main()
