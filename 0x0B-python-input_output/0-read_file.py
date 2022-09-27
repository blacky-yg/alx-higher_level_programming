#!/usr/bin/python3
"""Function that reads content from a file"""


def read_file(filename=""):
    """Prints the content of a file with UTF8 format"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
