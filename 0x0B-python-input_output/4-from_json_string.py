#!/usr/bin/python3
'''From json string module.'''


import json


def from_json_string(my_str):
    '''Returns an object represented by json string.'''

    return json.loads(my_str)
