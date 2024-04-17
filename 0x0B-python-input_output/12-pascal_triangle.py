#!/usr/bin/python3
'''Pascal triangle module.'''


def pascal_triangle(n):
    '''Returns a list of lists of integers representing
    the Pascal’s triangle of n.
    '''

    if (n <= 0):
        return []

    tris = [[1]]
    while len(tris) != n:
        tri = tris[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        tris.append(temp)
    return tris
