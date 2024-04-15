#!/usr/bin/python3
'''is_same_class module.'''


def is_same_class(obj, a_class):
    '''Returns if the object is exactly an instance of a class.'''

    if (type(obj) == a_class):
        return True
    return False
