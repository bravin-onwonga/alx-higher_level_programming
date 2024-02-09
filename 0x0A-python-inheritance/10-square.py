#!/usr/bin/python3
"""Class square the inherits from rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Takes an arg size and uses methods in super class
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
        super().area()
