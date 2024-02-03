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
            TypeError: if position length is less that 2 or if
                        one value is not an int
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

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

        Raises:
            TypeError: if value is not an integer or len(value) is not two
        """
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

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

        for _ in range(self.__position[1]):
            print()

        while (i < self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
            i += 1
