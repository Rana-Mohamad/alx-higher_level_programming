#!/usr/bin/python3
'''Rectangle module.'''


class Rectangle:
    '''Defines a rectangle.'''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''Constructor.

        Args:
            width: the rectangle width.
            height: the rectangle height.
        '''

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''Property to return the width of rectangle.'''

        return self.__width

    @width.setter
    def width(self, value):
        '''Property to set the width of the rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than zero.
        '''
        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if (value < 0):
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        '''Property to return the height of the rectangle.'''

        return self.__height

    @height.setter
    def height(self, value):
        '''Property to set the height of the rectangle.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than zero.
        '''

        if (type(value) is not int):
            raise TypeError("height must be an integer")

        if (value < 0):
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        '''Returns the rectangle area.'''

        return self.__width * self.__height

    def perimeter(self):
        '''Returns the rectangle perimeter.'''

        if (self.__width == 0 or self.__height == 0):
            return 0

        return ((self.__width + self.__height) * 2)

    def __str__(self):
        '''Returns the rectangle.'''

        string = ""

        if (self.__width == 0 or self.__height == 0):
            return string

        string += "\n".join(str(self.print_symbol) * self.__width
                            for h in range(self.__height))

        return string

    def __repr__(self):
        ''' Returns a string representation of the rectangle.'''

        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        '''Prints a message when an instance of Rectangle is deleted.'''

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Returns the biggest rectangle based on the area.'''

        if (not isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (not isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if (rect_1.area() >= rect_2.area()):
            return rect_1
        return rect_2
