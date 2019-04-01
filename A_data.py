"""
    A_data.py

    Name:  Sean Walker
    NetID: skw34

    Processes door swipe data for part A question 1.
"""


import csv


DATA_DIRECTORY = "../hw3_data/"
DOOR_DATA_FILENAME = DATA_DIRECTORY + "door_data.csv"
DOOR_DATA_NDAYS = 150
SIX_PM_MINUTES = 1080


def get_library_samples_labels(target_building_code):
    """
    Process door swipe data for book return decision tree classifier.
    """

    # training samples
    samples = [[0, 0] for _ in range(DOOR_DATA_NDAYS)]

    # number of returns (per day) for each library
    num_returns = 0

    # labels:
    # -1: "low-return day" (< 250 returns)
    #  1: "high-return day" (>= 250 returns)
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
                    labels[current_day] = 1
                else:
                    labels[current_day] = -1
                current_day += 1
                num_returns = 0

            # tally traffic for target building
            if row["building"] == target_building_code:
                samples[int(row["day"])][0] = int(row["day_of_week"])
                samples[int(row["day"])][1] += 1
                num_returns += int(row["is_book_return"])

    # label last day
    if num_returns >= 250:
        labels[current_day] = 1
    else:
        labels[current_day] = -1

    return (samples, labels)
