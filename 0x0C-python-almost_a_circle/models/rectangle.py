#!/usr/bin/python3
'''Rectangle module.'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor.

        Args:
            width: the rectangle width.
            height: the rectangle height.
        '''

        super.__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Returns the width.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets the width.'''
        self.__width = value

    @property
    def height(self):
        '''Returns the height.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets the height.'''
        self.__height = value

    @property
    def x(self):
        '''Returns x value.'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Sets x value.'''
        self.__x = value

    @property
    def y(self):
        '''Returns y value.'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Sets y value.'''
        self.__y = value
