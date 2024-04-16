#!/usr/bin/python3
'''MyInt module.'''


class MyInt(int):
    '''Rebel class inherits from int.'''

    def __eq__(self, num):
        '''Returns what was equal as not equal.'''

        return int(self) != num

    def __ne__(self, num):
        '''Returns what was not equal as equal.'''

        return int(self) == num
