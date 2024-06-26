#!/usr/bin/python3
'''Base module.'''
from json import dumps, loads


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
        if (list_objs is not None):
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding='UTF-8') as fl:
            fl.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        '''Returns list of the JSON string representation json_string.'''
        if (not json_string or json_string is None):
            return []
        else:
            return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Returns an instance with all attributes already set.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if (cls is Rectangle):
            new = Rectangle(3, 4)
        elif (cls is Square):
            new = Square(5)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances.'''
        from os import path
        file = "{}.json".format(cls.__name__)
        if (not path.isfile(file)):
            return []
        with open(file, "r", encoding='UTF-8') as fl:
            return [cls.create(**x) for x in cls.from_json_string(fl.read())]
