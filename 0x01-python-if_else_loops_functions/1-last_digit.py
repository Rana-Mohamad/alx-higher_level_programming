#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = str(number)[-1]
if (number < 0):
    lastDigit = -int(lastDigit)
if (int(lastDigit) > 5):
    print(
            "Last digit of {} is {} and is greater than 5"
            .format(number, int(lastDigit))
        )
elif (int(lastDigit) == 0):
    print(
            "Last digit of {} is {} and is 0"
            .format(number, int(lastDigit))
        )
elif (int(lastDigit) < 6) and (int(lastDigit) != 0):
    print(
            "Last digit of {} is {} and is less than 6 and not 0"
            .format(number, int(lastDigit))
        )
