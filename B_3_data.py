"""
    B_3_data.py

    Name:  Sean Walker
    NetID: skw34

    CPSC 310, Spring 2019
    Homework 3

    Processes door swipe and meal plan data for part B question 3.
"""


from collections import Counter
import csv


DATA_DIRECTORY = "../hw3_data/"
DOOR_DATA_FILENAME = DATA_DIRECTORY + "door_data.csv"
MEALPLAN_DATA_FILENAME = DATA_DIRECTORY + "meal_plan.csv"
MEALS_PER_WEEK = 14


def find_mealplan_nonusers():
    """
    Finds all students who on average use less than 50% of their meal swipes per
    week. Returns dictionary mapping student to their utilization as a floating
    point number.
    """
    # get all students with a meal plan
    mealplan_holders = set()
    with open(MEALPLAN_DATA_FILENAME, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["on_meal_plan"] == "1":
                mealplan_holders.add(row["student_id"])

    # find all students who only use 7 or fewer swipes per week (on average)
    # mapping of student id -> frequency of use
    students_dining_swipes = Counter(mealplan_holders)
    num_weeks = 0
    current_day_of_week = None
    with open(DOOR_DATA_FILENAME, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (row["is_dining_hall"] != "1" or
                    row["student_id"] not in mealplan_holders):
                continue

            if row["day_of_week"] == "0" and current_day_of_week != "0":
                # beginning of a new week
                num_weeks += 1
            current_day_of_week = row["day_of_week"]

            students_dining_swipes[row["student_id"]] += 1

    underutilizers = {}
    for student_id in mealplan_holders:
        utilization = students_dining_swipes[student_id] / \
            num_weeks / MEALS_PER_WEEK
        if utilization <= 0.5:
            underutilizers[student_id] = utilization

    return underutilizers
