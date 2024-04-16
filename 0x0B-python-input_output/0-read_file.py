#!/usr/bin/python3
'''Read file module.'''


def read_file(filename=""):
    '''Reads a text file.'''

    with open(filename, "r", encoding='UTF-8') as fl:
        print(fl.read())
