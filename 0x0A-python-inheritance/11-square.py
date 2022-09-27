#!/usr/bin/python3
"""Implementation of a Square object based on the Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Implementation based on Rectangle"""

    def __init__(self, size):
        """Initialisation of the Square

        Args:
            size (int): Size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """String representation of the Square

        Returns:
            str: String Representation
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
