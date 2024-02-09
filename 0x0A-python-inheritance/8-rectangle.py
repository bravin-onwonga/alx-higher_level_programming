#!/usr/bin/python3
"""Creates a simple class
"""


class BaseGeometry:
    """A simple class that does nothing"""
    def area(self):
        """A method that does nothing"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer

        Raises:
            TypeError - if value is not an integer
            ValueError - if value is less than or equal to zero
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
