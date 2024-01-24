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
        self.__size = size
        """
        Attributes:
            __size: private class attribute for class square
        """

    @property
    def size(self):
        """
        Returns: set attribute for class Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Attributes:
            value: public instance attribute for class square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns:
            The square of size
        """
        return (self.__size**2)

    def my_print(self):
        """
        Prints a square using the symbol #
        If size is zero then it prints an empty line
        """
        i = 0

        if (self.__size == 0):
            print()

        while (i < self.__size):
            print("#" * self.__size)
            i += 1
