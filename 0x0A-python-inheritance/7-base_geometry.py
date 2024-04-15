#!/usr/bin/python3
'''BaseGeometry module.'''


class BaseGeometry:
    '''BaseGeometry class.'''

    def area(self):
        '''Method to compute the area.'''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Integer validation method.

        Args:
            name: always a string.
            value: an integer number.
        '''

        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
