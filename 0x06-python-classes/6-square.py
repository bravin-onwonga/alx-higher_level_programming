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
    def __init__(self, size=0, position=(0, 0)):
        """
        Attributes:
            __size: private class attribute for class Square
            __position: private class attribute for class Square


        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        """
        self.__size = size
        self.__position = position
        if len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (self.__position[0] < 0 or self.__position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(self.__position[0]) or type(self.__position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        """
        Returns: set attribute for class Square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Attributes:
            value: public instance attribute position for class square
        """
        self.__position = value
        print(len(self.__position))

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

        if self.__position[1] > 0:
            print()

        while (i < self.__size):
            if self.__position[1] > 0:
                print("_" * self.__position[0], end="")
            else:
                print(" " * self.__position[0], end="")
            print("#" * self.__size)
            i += 1
