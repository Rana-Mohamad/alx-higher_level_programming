#!/usr/bin/python3
'''is_same_class module.'''


def is_same_class(obj, a_class):
    '''Determines if object is exactly an instance of a class.

    Returns:
        True: if the object is exactly an instance of the class.
        False: otherwise.
    '''

    return type(obj) == a_class
