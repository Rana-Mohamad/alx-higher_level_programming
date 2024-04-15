#!/usr/bin/python3
'''Square module.'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square class.'''

    def __init__(self, size):
        '''Constructor.

        Args:
            size: the square size.
        '''

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = sizeclass Square(Rectangle):
    '''Square class.'''

    def __init__(self, size):
        '''Constructor.

        Args:
            size: the square size.
        '''

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''Calc the square area.'''

        return self.__size * self.__size

    def __init__(self):
        '''Represent a string.'''

        return "[Square] " + str(self.__size) + "/" + str(self.__size)

    def area(self):
        '''Calc the square area.'''

        return self.__size * self.__size

    def __init__(self):
        '''Represent a string.'''

        return "[Square] " + str(self.__size) + "/" + str(self.__size)
