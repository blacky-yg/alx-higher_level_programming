#!/usr/bin/python3
"""Implementation of a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle
            x (int): The x coordinate of the rectangle
            y (int): The y coordinate of the rectangle
            id (int): The identity of the rectangle
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        super().__init__(id)
