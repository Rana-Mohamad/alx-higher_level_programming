#!/usr/bin/python3
'''Add two integers module.'''


def add_integer(a, b=98):
    '''Add two integers.

    Args:
        a: the first integer/float number.
        b: the second integer/float number, it takes  98 as default value.

    Raises:
        TypeError: if a, b not integer or float.

    Returns:
        The integer sum of the two values.
    '''

    if (type(a) not in (int, float)):
        raise TypeError("a must be an integer")
    if (type(b) not in (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
