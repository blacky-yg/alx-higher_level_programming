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

    def to_json(self, attrs=None):
        """Get a JSON representation of a student

        Args:
            attrs (Optional): A list of the attributes
        """
        if attrs is not None and all(isinstance(x, str) for x in attrs):
            data = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    data[key] = value
            return data
        else:
            return self.__dict__
