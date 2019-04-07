"""
    B_2_data.py

    Name:  Sean Walker
    NetID: skw34

    CPSC 310, Spring 2019
    Homework 3

    Processes door swipe data for part B question 2.
"""


from collections import Counter
import csv


COLLEGE_CODES = frozenset(["6", "7", "10", "17", "22", "26", "31", "46", "49",
                           "51", "62", "68", "70", "71"])
DATA_DIRECTORY = "../hw3_data/"
DOOR_DATA_FILENAME = DATA_DIRECTORY + "door_data.csv"
N_DAYS_IN_WEEK = 7


def get_last_college_per_day_tally():
    # engineer this so we go through the data set once
    # every time we read a row, we check the sid
    # we want to keep a dictionary of `student_id` -> [sunday's sleeping college, monday's sleeping college, ..., saturday's sleeping college]

    # to predict, just take the college they most commonly sleep in for a given day

    # dictionary mapping student id to the college they most recently swiped at
    students_most_recent_college_swipe = {}

    # dictionary mapping student id to a list of Counters of the different colleges they swipe at last for a given day
    last_college_swipe_per_day_tally = {}

    with open(DOOR_DATA_FILENAME, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        current_day = "0"
        current_day_of_week = "0"
        for row in reader:
            if row["building"] not in COLLEGE_CODES:
                # not a residential college swipe
                continue

            # first, check if we've moved on to a new day
            if row["day"] != current_day:
                # if so, we need to update all students' last-swipe tally
                for student_id in students_most_recent_college_swipe:
                    if not last_college_swipe_per_day_tally.get(student_id):
                        # initialize tally list for new entries
                        last_college_swipe_per_day_tally[student_id] = [
                            Counter() for _ in range(N_DAYS_IN_WEEK)]

                    # tally this day's swipe for this day of the week
                    building = students_most_recent_college_swipe[student_id]
                    tallies = last_college_swipe_per_day_tally[student_id]
                    tallies[int(current_day_of_week)][building] += 1

                # now update current day and day of the week
                current_day = row["day"]
                current_day_of_week = row["day_of_week"]

                # reset most recent swipe
                students_most_recent_college_swipe = {}

            # update most recent swipe for this student
            student_id = row["student_id"]
            students_most_recent_college_swipe[student_id] = row["building"]

    return last_college_swipe_per_day_tally
