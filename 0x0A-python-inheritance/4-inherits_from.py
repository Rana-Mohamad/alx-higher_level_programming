#!/usr/bin/python3
'''Inherits_from module.'''


def inherits_from(obj, a_class):
    '''Rreturns if the object is an instance of a class that\
            inherited (directly or indirectly).

    Args:
        obj: the object to check.
        a_class: the type to match the object.

    Returns:
        True: if the object is an instance of a class that inherited.
        False: otherwise.
    '''

    if (isinstance(obj, a_class) and type(obj) != a_class):
        return True
    return False
