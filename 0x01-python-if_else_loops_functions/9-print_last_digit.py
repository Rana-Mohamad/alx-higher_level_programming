#!/usr/bin/python3
def print_last_digit(number):
    number = str(number)[-1]
    number = int(number)
    print("{}".format(number), end="")
    return number
