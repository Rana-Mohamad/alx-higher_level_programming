#!/usr/bin/python3
'''Base unit tests module.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''Tests base class.'''

    def setup(self):
        '''Instantiates class.'''
        Base.Base_nb_objects = 0
        pass
