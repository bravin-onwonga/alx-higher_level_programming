#!/usr/bin/python3
"""
Function to read file"""
def read_file(filename=""):
    """
    Reads and print file content

    Args:
        filename - file to read and print
    """
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read())
