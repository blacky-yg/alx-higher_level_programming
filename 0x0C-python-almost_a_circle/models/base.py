#!/usr/bin/python3
"""Implementation of a Base class"""


class Base:
    """Representation of a Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of a new Base

        Args:
            id (int): The id of the new base
        """
        if (id is None):
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
