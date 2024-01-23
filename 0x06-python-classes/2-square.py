#!/usr/bin/python3
"""
class:
    A simple class  with a private attribute
"""


class Square:
    """
    Attributes:
        size: private class attribute for class square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than zero
    """
    def __init__(self, size=0):
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
