#!/usr/bin/python3
"""function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """
        divides all elements of a matrix.

        Args:
            matrix: list of lists of integers or floats
            div: a number (integer or float)

        Return: a new matrix with All elements of the matrix
        should be divided by div, rounded to 2 decimal places
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(error_msg)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(error_msg)
        for x in row:
            if not isinstance(x, int) and not isinstance(x, float):
                raise TypeError(error_msg)
    length = len(matrix[0])

    if length == 0:
        raise TypeError(error_msg)
    for row in matrix:
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix
