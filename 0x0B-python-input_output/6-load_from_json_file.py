#!/usr/bin/python3
"""Definition of a function that laod JSON from file"""
import json


def load_from_json_file(filename):
    """Load JSON from a file"""
    with open(filename) as f:
        return json.load(f)
