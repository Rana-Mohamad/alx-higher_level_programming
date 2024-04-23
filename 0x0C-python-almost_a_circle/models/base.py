#!/usr/bin/python3
'''Base module.'''
from json import dumps


class Base:
    '''Base class.'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor.'''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Returns the JSON string representation of list_dictionaries.'''
        if (not list_dictionaries or list_dictionaries is None):
            return "[]"
        else:
            return dumps(list_dictionaries)
