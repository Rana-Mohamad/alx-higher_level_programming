#!/usr/bin/python3
def best_score(a_dictionary):
    temp = 0
    key = ""
    if not a_dictionary:
        return None
    for i in a_dictionary:
        if (a_dictionary.get(i) > temp):
            temp = a_dictionary.get(i)
            key = i
    return key
