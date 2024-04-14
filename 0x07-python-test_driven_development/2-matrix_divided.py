#!/usr/bin/python3
'''Matrix devided module.'''


def matrix_divided(matrix, div):
    '''Devides all elements of the matrix by div.

    Args:
        matrix: the matrix.
        div: the number to devide matrix elements by.

    Raises:
        TypeError: if matrix elements is not integer or float
            or matrix rows has different size
            or div is not an integer or float number.
        ZeroDivisionError: if div equal zero.

    Returns:
        New matrix of devided elements rounded to 2 decimal places.
    '''

    size = len(matrix[0])
    for row in matrix:
        if (len(row) != size):
            raise TypeError("Each row of the matrix must have the same size")

        for x in row:
            if (type(x) not in (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    if (type(div) not in (int, float)):
        raise TypeError("div must be a number")

    if (div == 0):
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
