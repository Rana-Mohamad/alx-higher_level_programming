#!/usr/bin/python3
'''Append write module.'''


def append_write(filename="", text=""):
    '''Appends a string to file.'''

    with open(filename, "a", encoding='UTF-8') as fl:
        return fl.write(text)
