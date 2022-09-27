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
        super().__init__(size, size)
