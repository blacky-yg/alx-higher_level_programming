#!/usr/bin/python3
"""Definition of a function that converts string-to-JSON"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object"""
    return json.dumps(my_obj)
