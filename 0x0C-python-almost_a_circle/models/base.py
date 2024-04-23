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

    @classmethod
    def save_to_file(cls, list_objs):
        '''Writes the JSON string representation of list_objs to a file.'''
        if (list_objs) is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
            with open("{}.json".format(cls.__name__), "w", encoding='UTF-8')\
                    as fl:
                fl.write(cls.to_json_string(list_objs))
