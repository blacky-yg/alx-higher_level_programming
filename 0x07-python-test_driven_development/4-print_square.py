#!/usr/bin/python3
"""Defines a square-printing function."""


def print_square(size):
    """Print a square with the # character

    Args:
        size (int): The height/width of the square

    Raises:
        TypeError: Size is not an integer
        ValueError: Size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
