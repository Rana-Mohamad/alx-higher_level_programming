#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    else:
        for submatrix in matrix:
            if (len(submatrix) == 0):
                print()
            for i in range(len(submatrix)):
                print(
                        "{:d}".format(submatrix[i]),
                        end=" " if i != len(submatrix) - 1 else "\n"
                    )
            print()
