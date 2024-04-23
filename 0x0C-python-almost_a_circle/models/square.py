#!/usr/bin/python3
'''Square module.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor.'''

        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns a string.'''
        return "[{}] ({}) {}/{} - {}".\
               format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''Gets the size.'''
        return self.width

    @size.setter
    def size(self, value):
        '''Sets the size of the square.'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Assigns the arguments to the attributes.'''
        attrs = ["id", "size", "x", "y"]
        if args:
            for i, attr in enumerate(attrs):
                if (i < len(args)):
                    setattr(self, attr, args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
