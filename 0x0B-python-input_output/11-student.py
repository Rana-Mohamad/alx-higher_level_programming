#!/usr/bin/python3
'''Student module.'''


class Student:
    '''Student class.'''

    def __init__(self, first_name, last_name, age):
        '''Constructor.

        Args:
            first_name: the first name of the student.
            last_name: the last name of the student.
            age: the student age.
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Retrieves a dictionary representation.
        Args:
            attrs: the attributes to represent.
        '''

        if (type(attrs) is list and all(type(elm) is str for elm in attrs)):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        '''Replaces all attributes of the Student.'''

        for key, value in json.items():
            setattr(self, key, value)
