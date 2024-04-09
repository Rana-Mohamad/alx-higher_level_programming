#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dicts = sorted(list(a_dictionary.keys()))
    for i in dicts:
        print("{}: {}".format(i, a_dictionary.get(i)))
