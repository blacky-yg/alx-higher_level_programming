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
   if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(type(num) in [int, float] for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    new_matrix = [[eval("{:.2f}".format(num / div)) for num in row]
                  for row in matrix]
    return new_matrix
