#!/usr/bin/python3
"""Appends data to a file
"""


def append_write(filename="", text=""):
    """Appends data to a file, creates one if it doesn't exist

    Exeption Handled:
        FileNotFoundError - incase file doesn't exist

    Parameters:
        filename - name of file
        text - data to append type string

    Returns:
        number of characters written
    """
    try:
        with open(filename, 'a', encoding="utf-8") as my_file:
            return my_file.write(text)

    except FileNotFoundError:
        with open(filename, 'w', encoding="utf-8") as my_file:
            return my_file.write(text)
