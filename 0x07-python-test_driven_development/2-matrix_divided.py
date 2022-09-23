#!/usr/bin/python3
"""Defines a matrix division function"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix

    Args:
        matrix (list): List of list (ints or floats)
        div (int/float): Divisor

    Raises:
        TypeError: Contains rows of different sizes
        TypeError: Is not an int or float
        TypeError: Contains non-numbers
        ZeroDivisionError: If div is 0

    Returns:
        Result of the division
    """
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError(
            "Each row of the matrix must have the same size")
    matrix_divided = [x[:] for x in matrix]
    for line in matrix_divided:
        if len(line) != len(matrix_divided[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for i, elem in enumerate(line):
            if not isinstance(elem, (int, float)):
                raise TypeError(
                    'matrix must be a matrix (list of lists)'
                    ' of integers/floats'
                )
            line[i] = round(elem/div, 2)
    return matrix_divided
