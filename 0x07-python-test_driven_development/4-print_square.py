#!/usr/bin/python3
'''Print square module.'''


def print_square(size):
    '''Prints the square.

    Args:
        size: length of the side of the square.

    Raises:
        TypeError: if size is not an integer or less than 0.
        ValueError: if size is less than 0.
    '''

    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if (size == 0):
        print()
    else:
        for i in range(size):
            print("{}".format('#' * size))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
