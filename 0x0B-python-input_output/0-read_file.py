#!/usr/bin/python3
'''Read file module.'''


def read_file(filename=""):
    '''Reads a text file.'''

    with open(filename, "r", "UTF-8") as UTF8:
        UTF8.read()
