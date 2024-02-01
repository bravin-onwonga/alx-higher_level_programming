#!/usr/bin/python3
"""A simple class for a rectangle"""


class Rectangle:
    """defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Attributes:
            width: width of rectangle
            height: height of rectangle
        Raises:
            TypeError: width or height is not an integer
            ValueError: width or height is less than zero
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

        type(self).number_of_instances += 1

    @property
    def width(self):
        """getter property for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter property for width

        Attributes:
            value: value to set for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter property for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter property for height

        Attributes:
            value: value to set for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter of the rectangle
        """
        return (2 * (self.__width + self.__height))

    def __print__(self):
        """Prints a rectangle represented by #
        """
        if (self.__width != 0 and self.__height != 0):
            for i in range(self.__height):
                for k in range(self.__width):
                    print(self.print_symbol, end="")
                print()

    def __str__(self):
        """Prints the rectangle with the character #"""
        result = ""
        if (self.__width != 0 and self.__height != 0):
            for i in range(self.__height):
                for k in range(self.__width):
                    result += str(self.print_symbol)
                if (i != self.__height - 1):
                    result += '\n'
        return result

    def __repr__(self):
        """Return a string representation of the rectangle
        able to recreate a new instance by using eval()"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Deletes the object create"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
