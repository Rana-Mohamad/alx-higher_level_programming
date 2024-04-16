#!/usr/bin/python3
'''Write to file module.'''


def write_file(filename="", text=""):
    '''Writes to file and returns the number of charecters written.'''

    with open(filename, "r+", encoding='UTF-8') as fl:
        return fl.write(text)
