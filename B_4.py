"""
    B_4.py

    Name:  Sean Walker
    NetID: skw34

    CPSC 310, Spring 2019
    Homework 3

    Implements a k-nearest-neighbors classifer to find friends of a specified
    student.
"""


import math
from sklearn.neighbors import NearestNeighbors

from B_4_data import process_dining_data


NUM_FRIENDS = 5
TARGET_STUDENT_ID = "2969414704160674"


def run():
    samples, X, features_to_ids = process_dining_data(TARGET_STUDENT_ID)

    model = NearestNeighbors(n_neighbors=NUM_FRIENDS)

    model.fit(samples)

    friends = model.kneighbors(
        X, n_neighbors=NUM_FRIENDS, return_distance=False)

    print(f"Potential friends for {TARGET_STUDENT_ID}:")
    for friend in friends[0]:
        print(f"{features_to_ids[samples[friend]]}")
