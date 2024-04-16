#!/usr/bin/python3
'''Same class module.'''


def is_same_class(obj, a_class):
    '''Determines if object is exactly an instance of a classi.

    Returns:
            True or False
    '''

    return type(obj) == a_class
