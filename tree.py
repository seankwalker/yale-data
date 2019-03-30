"""
    tree.py

    Name:  Sean Walker
    NetID: skw34

    CPSC 310, Spring 2019
    Homework 3

    Implements a decision tree classifier to determine whether a given day is
    a "high-return" day (250 or more books returned) or a "low-return" day
    (fewer than 250 books returned).
"""

from sklearn import tree

from process_data import tree_process


BASS_LIBRARY_CODE = "3" # BASSLB
LAW_LIBRARY_CODE = "80" # YLL


def main():
    classifier = tree.DecisionTreeClassifier()
    bass_samples, bass_labels = tree_process(BASS_LIBRARY_CODE)
    law_samples, law_labels = tree_process(LAW_LIBRARY_CODE)

    # predict Bass:
    # "Bass Library on a Saturday with 2400 visitors by 6pm"
    classifier.fit(bass_samples, bass_labels)
    
    prediction = classifier.predict([[5, 2400]])[0]

    print("model predicts that Bass Library on a Saturday with 2400 visitors by 6pm will be a", end=" ")
    if prediction == 1:
        print("high-return day")
    elif prediction == -1:
        print("low-return day")
    else:
        print("ERROR WITH MODEL")

    # predict Law:
    # "the Law Library on a Thursday with 450 visitors by 6pm"
    classifier.fit(law_samples, law_labels)

    prediction = classifier.predict([[3, 450]])[0]

    print("model predicts that the Law Library on a Thursday with 450 visitors by 6pm will be a", end=" ")
    if prediction == 1:
        print("high-return day")
    elif prediction == -1:
        print("low-return day")
    else:
        print("ERROR WITH MODEL")


if __name__ == "__main__":
    main()
