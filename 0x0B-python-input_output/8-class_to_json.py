#!/usr/bin/python3
"""Definition of a function that converts a class to JSON"""


def class_to_json(obj):
    """Return the dictionary of an object"""
    return obj.__dict__
