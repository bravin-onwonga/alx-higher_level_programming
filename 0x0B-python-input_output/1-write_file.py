#!/usr/bin/python3
"""
Function to write text to a file
"""


def write_file(filename="", text=""):
    """
    Opens and writes txt to a file, creates one if file doesn't exist

    Parameters:
        filename - name of file
        text - text to write

    Returns:
        number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as my_file:
        written_chars = my_file.write(text)

    return written_chars
