#!/usr/bin/python3
"""
class:
    Square: A simple class  with a private attribute
"""


class Square:
    """
    class:
        Square: A simple class  with a private attribute
    """
    def __init__(self, size=0):
        """
        Attributes:
            size: private class attribute for class square
        """
        self.__size = size

    def size(self, value):
        """
        Attributes:
            value: private instance attribute for class square

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
        """
        Returns: set attribute for class Square
        """
        return self.__size


    def area(self):
        """
        Returns:
            The square of size
        """
        return (self.__size**2)
