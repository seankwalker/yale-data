"""
    A.py

    Name:  Sean Walker
    NetID: skw34

    CPSC 310, Spring 2019
    Homework 3

    Implements a decision tree classifier to determine whether a given day is
    a "high-return" day (250 or more books returned) or a "low-return" day
    (fewer than 250 books returned).
"""


import graphviz
from sklearn import tree

from A_data import get_library_samples_labels


BASS_LIBRARY_CODE = "3"  # BASSLB
LAW_LIBRARY_CODE = "80"  # YLL


def make_prediction(labels, library_name, samples, X):
    """
    Uses a decision tree classifier to predict the result for `X`, given the
    sample data `samples` and class labels `labels`.
    """

    # make prediction based on data
    classifier = tree.DecisionTreeClassifier()
    classifier.fit(samples, labels)
    prediction = classifier.predict(X)[0]

    # model decision tree
    dot_data = tree.export_graphviz(classifier,
                                    feature_names=[
                                        "day of the week", "library traffic"],
                                    class_names=[
                                        "low-return day", "high-return day"],
                                    filled=True, rounded=True,
                                    special_characters=True)
    graph = graphviz.Source(dot_data)
    graph.render(library_name)

    print(f"prediction for {library_name}: {prediction}")
    return prediction


def main():
    """
    Processes data and predicts result for specified situation at Bass and Law
    libraries.
    """

    bass_samples, bass_labels = get_library_samples_labels(BASS_LIBRARY_CODE)
    law_samples, law_labels = get_library_samples_labels(LAW_LIBRARY_CODE)

    # "Bass Library on a Saturday with 2400 visitors by 6pm"
    prediction = make_prediction(bass_labels, "Bass Library", bass_samples,
                                 [[5, 2400]])

    print("Bass Library on a Saturday with 2400 visitors by 6 p.m. is predicted",
          "to be a", end=" ")
    if prediction == 1:
        print("high-return day")
    elif prediction == -1:
        print("low-return day")

    # "the Law Library on a Thursday with 450 visitors by 6pm"
    prediction = make_prediction(law_labels, "Law Library", law_samples,
                                 [[3, 450]])

    print("Law Library on a Thursday with 450 visitors by 6 p.m. is predicted",
          "to be a", end=" ")
    if prediction == 1:
        print("high-return day")
    elif prediction == -1:
        print("low-return day")


if __name__ == "__main__":
    main()
