#!/usr/bin/python3
'''Square module.'''


class Square:
    '''Define a square.'''

    def __init__(self, size=0):
        '''Constructor.

        Args:
            size: length of the side of the square.
        '''
        self.size = size

    def area(self):
        '''Calculate the area of the square.

        Returns:
            The square area
        '''
        return self.__size * self.__size

    @property
    def size(self):
        '''Property to return the size of the side of the square.'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Property to set the size of the square.

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        '''Prints the square.'''
        for i in range(self.size):
            print("{}".format('#'*self.size))
