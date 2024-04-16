#!/usr/bin/python3
'''Load from json file module.'''


import json


def load_from_json_file(filename):
    '''Creates an object from json file.'''

    with open(filename, "r", encoding="UTF-8") as fl:
        return json.load(fl)
