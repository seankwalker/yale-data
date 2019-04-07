"""
    B_3.py

    Name:  Sean Walker
    NetID: skw34

    CPSC 310, Spring 2019
    Homework 3

    Generates an email message for specified student to remind them to use more
    of their meal swipes.
"""


from B_3_data import find_mealplan_nonusers


MEALS_PER_WEEK = 14


def run():
    underutilizers = find_mealplan_nonusers()

    target_student_id = "7143237956228680"
    print(write_email(target_student_id, underutilizers[target_student_id]))


def write_email(student_id, student_mealplan_utilization):
    message = f"Dear {student_id},\nYou are only using " + \
        f"{round(student_mealplan_utilization * MEALS_PER_WEEK)} of your " + \
        "allotted meals per week.\n\nSincerely,\nYale Dining"

    return message
