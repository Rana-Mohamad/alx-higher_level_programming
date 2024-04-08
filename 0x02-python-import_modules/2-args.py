#!/usr/bin/python3
if (__name__ == "__main__"):
    import sys

    argsNum = len(sys.argv) - 1
    if (argsNum == 1):
        print("1 argument:")
    elif (argsNum == 0):
        print("0 arguments.")
    else:
        print("{} arguments:".format(argsNum))
    for x in range(argsNum+1):
        print("{}: {}".format(x, sys.argv[i]))
