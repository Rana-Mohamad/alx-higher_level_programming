#!/usr/bin/python3
'''Add attribute module.'''


def add_attribute(obj, attr, value):
    '''Add attribute to an object if possible.

    Args:
        obj: the object to add to.
        attr: the attribute to add to obj.
        value: the value of attr.

    Raises:
        TypeError: if the object can't have a new attr.
    '''

    if (hasattr(obj, "__dict__")):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
