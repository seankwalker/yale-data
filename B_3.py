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


def run():
    underutilizers = find_mealplan_nonusers()

    target_student_id = "7143237956228680"
    print(write_email(target_student_id, underutilizers[target_student_id]))


def write_email(student_id, student_mealplan_utilization):
    message = f"Hello, {student_id}!\n\nThis is an automated message from " + \
        "Yale Dining.\n\nWe just wanted to inform you that according to our" + \
        " statistics, you've only been using about " + \
        f"{round(student_mealplan_utilization * 100)}% of your meal swipes " + \
        "per week (on average)!\n\nLove,\n\nYale Dining Bot"

    return message
