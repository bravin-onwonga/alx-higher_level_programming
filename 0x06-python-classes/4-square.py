#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size

    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def size(self):
        return self.__size

    def area(self):
        res = self.__size**2
        return (res)
