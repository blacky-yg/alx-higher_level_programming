#!/usr/bin/python3
"""Definition of function that converts JSON to object"""
import json


def from_json_string(my_str):
    """Return the object representation of a JSON"""
    return json.loads(my_str)
