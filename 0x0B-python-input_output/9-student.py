#!/usr/bin/python3
"""Definition of a Student"""


class Student:
    """Representation of a student"""

    def __init__(self, first_name, last_name, age):
        """Initialization a new student

        Args:
            first_name (str): The first name
            last_name (str): The last name
            age (int): The age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a JSON representation of a student"""
        return self.__dict__
