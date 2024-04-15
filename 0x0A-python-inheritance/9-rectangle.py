#!/usr/bin/python3
'''Rectangle module.'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class.'''

    def __init__(self, width, height):
        '''Constructor.

        Args:
            width: the rectangle width.
            height: the rectnagle height.
        '''

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area():
        '''Returns rectangle area.'''

        return self.__width * self.__height

    def __str__(self):
        '''String representation.'''

        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
