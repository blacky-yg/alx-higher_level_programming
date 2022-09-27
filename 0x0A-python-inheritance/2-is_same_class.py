#!/usr/bin/python3
"""Implementation of comparison between classes"""


def is_same_class(obj, a_class):
    """Implementation of comparison between classes

    Args:
        obj (Any): The object to check
        a_class (type): The type to check

    Returns:
        boolean: True or False
    """
    return type(obj) == a_class
