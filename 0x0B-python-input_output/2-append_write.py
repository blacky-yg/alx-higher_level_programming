#!/usr/bin/python3
"""Function that append content to a file"""


def write_file(filename="", text=""):
    """Appends a content to the end of a text file

    Args:
        filename (str): The name of the file to append to
        text (str): The content to append to the file

    Returns:
        The number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
