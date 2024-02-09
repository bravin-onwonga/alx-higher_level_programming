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
        if not name and not value:
            raise TypeError("BaseGeometry.integer_validator() missing 2 required positional arguments: 'name' and 'value'")
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
