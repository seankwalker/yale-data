"""
    B.py

    Name:  Sean Walker
    NetID: skw34

    CPSC 310, Spring 2019
    Homework 3

    Finds a student with a regular appointment at Yale Health.
"""


from B_1_data import find_regular_appointment_at


DAYS_OF_WEEK = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday"]
YALE_HEALTH_CODE = "79"  # YHC


def run():
    student_id, day_of_week, time = find_regular_appointment_at(
        YALE_HEALTH_CODE)
    print(f"student with id {student_id} has a regular Yale Health appointment",
          f"on {DAYS_OF_WEEK[int(day_of_week)]} at",
          f"{int(time)//60}:{int(time)%60}")
