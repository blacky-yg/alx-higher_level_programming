#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with it's size

        Args:
            size (int): The size of the square
            position (int, int): The position of the new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter and setter for the square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter for the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculatate the current area of the square"""
        return (self.__size * self.__size)

    def __ne__(self, other):
        """Redefine != comparison to a square"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Redefine < comparison to a square"""
        return self.area() < other.area()

    def __gt__(self, other):
        """Redefine > comparison to a square"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Redefine >= compmarison to a square"""
        return self.area() >= other.area()

    def __eq__(self, other):
        """Redefine == comparision to a square"""
        return self.area() == other.area()

    def __le__(self, other):
        """Redefine <= comparison to a square"""
        return self.area() <= other.area()
