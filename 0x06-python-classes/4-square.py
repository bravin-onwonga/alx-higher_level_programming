#!/usr/bin/python3
"""
class:
    A simple class  with a private attribute
"""


class Square:
    def __init__(self, size=0):
        self.__size = size

    def size(self, value):
        """
        Attributes:
            size: private class attribute for class square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def size(self):
        return self.__size

    """
    Returns:
        The square of size
    """
    def area(self):
        res = self.__size**2
        return (res)
