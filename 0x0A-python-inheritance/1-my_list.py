#!/usr/bin/python3
'''MyList module.'''


class MyList(list):
    '''MyList class.'''

    def print_sorted(self):
        '''Function to print sorted list.'''

        print(sorted(self))
