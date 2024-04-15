#!/usr/bin/python3
'''Rectangle module.'''


class Rectangle:
    '''Defines a rectangle.'''

    def __init__(self, width=0, height=0):
        '''Constructor.

        Args:
            width: the rectangle width.
            height: the rectangle height.
        '''

        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''Property to return the width of rectangle.'''

        return int(self.__width)

    @width.setter
    def width(self, value):
        '''Property to set the width of the rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than zero.
        '''
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")

        if (value < 0):
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        '''Property to return the height of the rectangle.'''

        return int(self.__height)

    @height.setter
    def height(self, value):
        '''Property to set the height of the rectangle.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than zero.
        '''

        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")

        if (value < 0):
            raise ValueError("height must be >= 0")

        self.__height = value

    @classmethod
    def rectangle(cls, Rectangle):
        return cls, Rectangle
