#!/usr/bin/python3
'''Square module.'''


class Square:
    '''Define a square.'''

    def __init__(self, size=0, position=(0, 0)):
        '''Constructor.

        Args:
            size: length of the side of the square.
            position: the position of the square.
        '''
        self.size = size
        self.position = position

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
        if (self.__size == 0):
            print()
            return
        for j in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            print("{}".format('#'*self.__size))

    @property
    def position(self):
        '''Property to return the position.'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Property to set the position.

        Raises:
            TypeError: of tuple was not two positive integer values
        '''
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
