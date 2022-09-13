#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a square with it's size

        Args:
            size (int): The size of the square
        """
        self.size = size

    @property
    def size(self):
        """Getter and setter for the square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculatate the current area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Display the square with #"""
        for i in range(0, self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
