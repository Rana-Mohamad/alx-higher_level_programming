#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dicts = {}
    for key in a_dictionary:
        dicts[key] = a_dictionary.get(key) * 2
    return dicts
