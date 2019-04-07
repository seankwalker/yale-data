"""
    B_4_data.py

    Name:  Sean Walker
    NetID: skw34

    CPSC 310, Spring 2019
    Homework 3

    Processes door swipe data for part B question 4.
"""


from collections import Counter
import csv


COLLEGE_CODES = ("6", "7", "10", "17", "22", "26", "31", "46", "49", "51", "62",
                 "68", "70", "71")
DATA_DIRECTORY = "../hw3_data/"
DOOR_DATA_FILENAME = DATA_DIRECTORY + "door_data.csv"


def process_dining_data(target_student_id):
    """

    Consider last dining hall swipe for a day to be a dinner swipe.

    Can get, for each person per day:
        - which dhall
        - time

    i.e. 3 features for a person

    So now we have 150 samples, 2 features for 12,400 people.

    Reduce the 150 samples into one for each person:
        - one feature per dhall for # times they swiped there
        - average dinner swipe time
    """

    # the dining hall and time for the student's most recent dinner
    most_recent_dinners = {}

    # for each `student_id`, a counter of their visits to various dining halls
    # and a list of all their dinner times (to be averaged at the end)
    dinner_data_tally = {}
    current_day = 0
    with open(DOOR_DATA_FILENAME, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # only care about dining hall swipes between 5pm and 8pm
            if (row["is_dining_hall"] != "1" or
                    int(row["time_of_day"]) <= 1020 or
                    int(row["time_of_day"]) >= 1200):
                continue

            # check if we've moved to the next day
            if row["day"] != str(current_day):
                # if so, save all the dinner data from the previous day
                for student_id, dinner in most_recent_dinners.items():
                    if not dinner_data_tally.get(student_id):
                        # init: zero dinners at each college, no dinner times
                        dinner_data_tally[student_id] = list(
                            [0 for _ in range(len(COLLEGE_CODES))] + [[]])
                    else:
                        dinner_data_tally[student_id][COLLEGE_CODES.index(
                            dinner[0])] += 1
                        dinner_data_tally[student_id][-1].append(dinner[1])
                current_day += 1

            most_recent_dinners[row["student_id"]] = [row["building"],
                                                      int(row["time_of_day"])]

    # calculate average dinner time
    dinners = {}
    for student_id, dinner_data in dinner_data_tally.items():
        dinner_times = dinner_data_tally[student_id][-1]
        dinners[student_id] = tuple(
            dinner_data_tally[student_id][0:-1] +
            [round(sum(dinner_times)/len(dinner_times))])

    # remove target from sample data
    target_student_data = [dinners["2969414704160674"]]
    dinners.pop("2969414704160674")

    # create a dictionary mapping features to student id, so as to identify
    # closest friends' student ids
    features_to_ids = {}
    for student_id, features in dinners.items():
        features_to_ids[features] = student_id

    # return as a N x 2 array (where N = number of students)
    # also return the data for `target_student_id` so their closest friends
    # can be predicted
    return ([dinner for _, dinner in dinners.items()], target_student_data,
            features_to_ids)
