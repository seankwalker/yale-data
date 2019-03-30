"""
    process_data.py

    Name:  Sean Walker
    NetID: skw34

    CPSC 310, Spring 2019
    Homework 3

    Processes raw data into forms usable for individual tasks.
"""


import csv


# constants
DATA_DIRECTORY = "../hw3_data/"

BUILDING_CODES_FILENAME = DATA_DIRECTORY + "building_codes.csv"
DOOR_DATA_FILENAME = DATA_DIRECTORY + "door_data.csv"
MEAL_DATA_FILENAME = DATA_DIRECTORY + "meal_plan.csv"

DOOR_DATA_NDAYS = 150
SIX_PM_MINUTES = 1080

def tree_process(target_building_code):
    """
    Process door swipe data for book return decision tree classifier.

    Input format:
    day,day_of_week,student_id,time_of_day,building,is_dining_hall,is_book_return

    Output format: a 150x2 array filled with, for each day (0-149):
                        - the day of the week (0-6), and
                        - the amount of library traffic for that day
    """

    # training samples
    samples = [[0, 0] for _ in range(DOOR_DATA_NDAYS)]

    # number of returns (per day) for each library
    num_returns = 0

    # labels:
    # 0: "low-return day" (< 250 returns)
    # 1: "high-return day" (>= 250 returns)
    labels = [0 for _ in range(DOOR_DATA_NDAYS)]

    # tally up data for specified building code
    current_day = 0
    with open(DOOR_DATA_FILENAME, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # only count library traffic until 6:00 PM
            if int(row["time_of_day"]) >= SIX_PM_MINUTES:
                continue

            # determine whether the previous day was high/low return
            if row["day"] != str(current_day):
                if num_returns >= 250:
                    labels[current_day] = -1
                else:
                    labels[current_day] = 1
                current_day += 1
                num_returns = 0

            # tally traffic for target building
            if row["building"] == target_building_code:
                samples[int(row["day"])][0] = int(row["day_of_week"])
                samples[int(row["day"])][1] += 1
                num_returns += int(row["is_book_return"])

    return (samples, labels)


if __name__ == "__main__":
    tree_process()
