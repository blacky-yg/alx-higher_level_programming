#!/usr/bin/python3
"""Implementation of a custom list object"""


class MyList(list):
    """Custom List"""

    def print_sorted(self):
        """Prints the ascending sorted list"""
        print(sorted(self))
