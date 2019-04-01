"""
    B_4_data.py

    Name:  Sean Walker
    NetID: skw34

    CPSC 310, Spring 2019
    Homework 3

    Processes door swipe data for part B question 4.
"""


import csv


DATA_DIRECTORY = "../hw3_data/"
DOOR_DATA_FILENAME = DATA_DIRECTORY + "door_data.csv"


def process_dining_data():
    """

    Consider last dining hall swipe for a day to be a dinner swipe.

    Can get, for each person per day:
        - which dhall
        - time
        - day of week

    i.e. 3 features for a person

    So now we have 150 samples, 3 features for 12,400 people.


    Our goal is obviously: given one person, find the 5 people with closest "dining habits"

    So we need to make a feature "dining habits"

    just flatten each student to one array

    """

    # first, get all student ids
    student_ids = set()
    with open(DOOR_DATA_FILENAME, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            student_ids.add(row["student_id"])

    # next, record the dinner data for every student
    current_day = 0
    most_recent_dinners = dict.fromkeys(student_ids, [None, None, None])
    dinners = dict.fromkeys(student_ids, [])
    student_by_dinners = {}

    with open(DOOR_DATA_FILENAME, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # only care about dining swipes
            if row["is_dining_hall"] != "1":
                continue

            # check if we've moved to the next day
            if row["day"] != str(current_day):
                # if so, save all the dinner data from the previous day
                for student_id in student_ids:
                    dinners[student_id] += most_recent_dinners[student_id]

                    # reset meal to `None` for the next day
                    # (it already is this if they didn't swipe for dinner today,
                    # but that happens rarely, so checking would probably be
                    # worse performance)
                    most_recent_dinners[student_id] = [None, None, None]

                current_day += 1

            # update most recent dinner swipe: must be between 5pm and 8pm
            # could improve granularity here by making sure they're swiping
            # at the exact dinner times for every college and given the day of
            # the week, e.g. 5-7:30pm for a Hopper Tuesday
            if (int(row["time_of_day"]) <= 1020 or
                    int(row["time_of_day"]) >= 1200):
                continue

            most_recent_dinners[row["student_id"]] = [row["building"],
                                                      row["time_of_day"],
                                                      row["day_of_week"]]

    # now we have our data: 12,400 150x1 lists of "dinner habits"
    return dinners
