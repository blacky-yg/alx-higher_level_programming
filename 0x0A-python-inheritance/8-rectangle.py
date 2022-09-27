#!/usr/bin/python3
"""Implementation of a Rectangle object based on the BaseGeometry"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Implementation based on BaseGeometry"""

    def __init__(self, width, height):
        """Initialisation of the Rectangle

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
