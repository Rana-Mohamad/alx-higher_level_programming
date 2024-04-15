#!/usr/bin/python3
'''Inherits_from module.'''


def inherits_from(obj, a_class):
    '''Rreturns if the object is an instance of a class that\
            inherited (directly or indirectly) from the specified class.
    '''
    return isinstance(obj, a_class) and type(obj) != a_class