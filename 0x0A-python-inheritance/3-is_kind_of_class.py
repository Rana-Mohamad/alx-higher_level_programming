#!/usr/bin/python3
'''Kind of class module.'''


def is_kind_of_class(obj, a_class):
    '''Determines if object is an instance of, or if the object is an\
            instance of a class that inherited from, the class.
    '''

    return isinstance(obj, a_class)
