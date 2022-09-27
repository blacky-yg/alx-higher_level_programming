#!/usr/bin/python3
"""Implements an object skeleton for BaseGeometry"""


class BaseGeometry:
    """Implementation of the Object Skeleton"""

    def area(self):
        """Calculate the area of the BaseGeometry

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check Integer before the area calculation

        Args:
            name (str): The name of the variable
            value (any): The value to check

        Raises:
            ValueError: value must be greater than 0
            TypeError: value must be an integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
