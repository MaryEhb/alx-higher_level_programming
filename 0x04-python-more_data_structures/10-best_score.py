#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) is 0:
        return None

    score = 0
    for i in a_dictionary:
        if a_dictionary[i] > score:
            score = a_dictionary[i]

    return score
