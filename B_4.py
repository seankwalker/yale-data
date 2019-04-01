"""
    B_4.py

    Name:  Sean Walker
    NetID: skw34

    CPSC 310, Spring 2019
    Homework 3

    Implements a k-nearest-neighbors classifer to find friends of a specified
    student.
"""


import numpy as np
from sklearn.neighbors import NearestNeighbors

from B_4_data import process_dining_data


NUM_FRIENDS = 5


def dining_habits_distance(X, Y):
    """
    Defines the "distance" between two students' dining habits.

    Each dining habits array (`X`, `Y`) should be a 450 x 1 array which consists
    of 3-tuples: each 3-tuple contains the following information:
        (1) Dinner Location Code
        (2) Dinner Time
        (3) Dinner Day of Week

    Distance is calculated as follows. For a given 3-tuple, the following rules
    are applied:
        - if (1) is different, 1. else,
        - if (2) above is more than 10 minutes different, 1. else,
        - they ate at the same time in the same location: 0.

    The total distance of dining habits is the sum of the scores of all the
    dinner 3-tuples.
    """

    distance = 0
    for i in range(0, len(X), 3):
        if X[i] != Y[i] or abs(X[i+1] - Y[i+1]) > 10:
            distance += 1
    return distance


def run():
    dinners = process_dining_data()
    samples = [student_dinners for student, student_dinners in dinners.items()]

    model = NearestNeighbors(n_neighbors=NUM_FRIENDS,
                             metric=dining_habits_distance)

    model.fit(samples)

    friends = model.kneighbors(dinners["2969414704160674"],
                               n_neighbors=NUM_FRIENDS, return_distance=False)

    print(f"friends: {friends}")
