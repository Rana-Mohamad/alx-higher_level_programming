#!/usr/bin/python3
'''Is same class module.'''


def is_same_class(obj, a_class):
    '''Returns True if the object is exactly an instance \
            of the specified class ; otherwise False.
    '''

    return type(obj) == a_class
