#!/usr/bin/python3
"""
Returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """Return a list of attributes and methods of the given object

    Args:
        obj (Any): Object of any type

    Returns:
        list: list containing all the attributes and members functions
    """
    return dir(obj)
