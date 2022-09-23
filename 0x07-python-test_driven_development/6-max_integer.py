#!/usr/bin/python3
"""Find the max integer in a list"""


def max_integer(list=[]):
    """Find and return the max int"""

    if len(list) == 0:
        return None
    res = list[0]
    i = 1
    while i < len(list):
        if list[i] > res:
            res = list[i]
        i += 1
    return res
