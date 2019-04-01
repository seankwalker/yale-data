"""
    B_2.py

    Name:  Sean Walker
    NetID: skw34

    CPSC 310, Spring 2019
    Homework 3

    Implements a decision tree classifer to predict which residential college
    a student will sleep in every night of the week.
"""


from B_2_data import get_last_college_per_day_tally


DAYS_OF_WEEK = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday"]


def run():
    tallies = get_last_college_per_day_tally()
    student_ids = tallies.keys()

    # construct a dictionary mapping sleeping schedule -> student id
    # s.t. we can easily find students with matching schedules

    # also, remove all schedules where the student is predicted to sleep in
    # the same college every night

    heterogeneous_sleeping_schedules = {}

    for student_id in student_ids:
        tally = tallies[student_id]
        schedule = tuple([days_sleeping_locations.most_common(
            1)[0][0] for days_sleeping_locations in tally])

        # remove entries where the student is predicted to sleep in the same
        # college every night
        # (making the list a set removes duplicates; if there's <= 1 entry
        # in that set, it means there was only maximum of one value in the list)
        if len(set(schedule)) <= 1:
            continue

        # check if this sleeping schedule overlaps with someone else
        if heterogeneous_sleeping_schedules.get(schedule):
            print(f"overlap in schedule found!", end=" | ")
            print(f"student {student_id} has the same schedule as",
                  f"{heterogeneous_sleeping_schedules.get(schedule)}")
            print(f"schedule: {schedule}")
        else:
            heterogeneous_sleeping_schedules[schedule] = student_id
