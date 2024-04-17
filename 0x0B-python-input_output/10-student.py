#!/usr/bin/python3
'''Student module.'''


class Student:
    '''Student class.'''

    def __init__(self, first_name, last_name, age):
        '''Constructor.'''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Retrieves a dictionary representation.
        Args:
            attrs: the attributes to represent.
        '''

        if (type(attrs) is list and all(type(elm) is str for elm in attrs)):
            return [key: getattr(self, key)
                    for key in attrs if hasattr(self, key)]
        return self.__dict__
