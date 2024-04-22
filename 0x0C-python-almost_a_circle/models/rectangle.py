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

        super().__init__(id)
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
        self.validation(value, "width")
        self.__width = value

    @property
    def height(self):
        '''Returns the height.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets the height.'''
        self.validation(value, "height")
        self.__height = value

    @property
    def x(self):
        '''Returns x value.'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Sets x value.'''
        self.validation(value, "x", False)
        self.__x = value

    @property
    def y(self):
        '''Returns y value.'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Sets y value.'''
        self.validation(value, "y", False)
        self.__y = value

    def validation(self, value, attrname, flag=True):
        '''Method to validate the value.'''
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(attrname))
        elif (flag and value <= 0):
            raise ValueError("{} must be > 0".format(attrname))
        elif (not flag and value < 0):
            raise ValueError("{} must be >= 0".format(attrname))

    def area(self):
        '''Calculate the rectangle area.'''
        return self.__width * self.__height

    def display(self):
        '''Returns the rectangle.'''
        string = "\n" * self.__y +\
                 (' ' * self.__x + '#' * self.__width + "\n") * self.__height
        print(string, end='')

    def __str__(self):
        '''Returns a string.'''
        return "[{}] ({}) {}/{} - {}/{}".\
            format(type(self).__name__, self.__id, self.__x,
                   self.__y, self.__width, self.__height)
