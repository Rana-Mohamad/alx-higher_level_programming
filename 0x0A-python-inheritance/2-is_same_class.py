#!/usr/bin/python3
'''Same class module.'''


def is_same_class(obj, a_class):
    '''Returns if object is exactly an instance of a class.

    Args:
        obj: the object to check.
        a_class: the type to match the object.
    '''

    return type(obj) is a_class
