#!/usr/bin/python3
"""Check if an object is an instance of a specific class that inherited"""


def is_kind_of_class(obj, a_class) -> bool:
    """Implementation of object is instance of a class that inherited

    Args:
        obj (Any): The object to check
        a_class (type): The type to check against

    Returns:
        boolean: True or False
    """
    return type(obj) != a_class and issubclass(type(obj), a_class)
