#!/usr/bin/python3
'''Square module.'''


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''Square class.'''

    def __init__(self, size):
        '''Constructor.

        Args:
            size: the square size.
        '''

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area():
        '''Calc the square area.'''

        return self.__size * self.__size
