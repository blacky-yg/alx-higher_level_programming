#!/usr/bin/python3
"""Defines a printing name function."""


def say_my_name(first_name, last_name=""):
    """Print a name with first_name and last_name

    Args:
        first_name (str): The first name
        last_name (str): The last name

    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
