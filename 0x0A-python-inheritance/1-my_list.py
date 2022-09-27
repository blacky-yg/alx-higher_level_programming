#!/usr/bin/python3
"""Implementation of a custom list object"""


class MyList(list):
    """Custom List"""

    def __init__(self):
        """Initialization of the custom list"""
        super().__init__()

    def print_sorted(self):
        """Prints the ascending sorted list"""
        print(sorted(self))
