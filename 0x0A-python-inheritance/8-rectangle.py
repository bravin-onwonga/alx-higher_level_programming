#!/usr/bin/python3
"""A class that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
