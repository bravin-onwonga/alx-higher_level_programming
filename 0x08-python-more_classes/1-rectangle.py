#!/usr/bin/python3
"""A simple class"""


class Rectangle:
    """defines a rectangle"""
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
        self.__height = value
