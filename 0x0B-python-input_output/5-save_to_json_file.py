#!/usr/bin/python3
'''Save to json file module.'''


import json


def save_to_json_file(my_obj, filename):
    '''Writes an Object to a text file, using a JSON representation.'''

    with open(filename, "w", encoding="UTF-8") as fl:
        json.dump(my_obj, fl)
