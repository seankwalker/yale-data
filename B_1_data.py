"""
    B_1_data.py

    Name:  Sean Walker
    NetID: skw34

    CPSC 310, Spring 2019
    Homework 3

    Processes door swipe data for part B question 1.
"""


from collections import Counter
import csv


DATA_DIRECTORY = "../hw3_data/"
DOOR_DATA_FILENAME = DATA_DIRECTORY + "door_data.csv"
DOOR_DATA_NDAYS = 150


def round_to_nearest_half_hour(mins):
    """
    Rounds time (`mins`) to nearest half-hour increment.

    Adapted from tzaman's response here: https://stackoverflow.com/a/29545984
    """
    n = int(mins) + 15
    return str(n - (n % 30))


def find_regular_appointment_at(target_building_code):
    """
    Process door swipe data to return a student who regularly goes to
    `target_building_code` at the same day and time each week.
    """

    # keep a list of potential regular appointments
    appointments = Counter()

    with open(DOOR_DATA_FILENAME, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["building"] != target_building_code:
                continue

            student_id = row["student_id"]
            day_of_week = row["day_of_week"]

            # let's assume yale health appointments start at either the start
            # of the hour or at the half, e.g. 12:00, 12:30, 1:00, 1:30, ...
            # consider each swipe to round to the nearest half-hour increment,
            # as it'd be very rare for someone to be 30 minutes or more late
            swipe_time = row["time_of_day"]
            presumed_appt_time = round_to_nearest_half_hour(swipe_time)

            # if we assume each swipe is a student showing up for an appointment
            # then the actual regular appointments will get noticeably high
            # tallies; obviously there will be a lot of one-off visits too,
            # but we only care about the high-tally results
            presumed_appt = (student_id, day_of_week, presumed_appt_time)
            appointments[presumed_appt] += 1

    # return the appointment most regularly attended
    return appointments.most_common(1)[0][0]
