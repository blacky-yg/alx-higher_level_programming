#!/usr/bin/python3
"""Function that write content to a file"""


def write_file(filename="", text=""):
    """Write a content to a text file

    Args:
        filename (str): The name of the file to create
        text (str): The content to write to the file

    Returns:
        The number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
