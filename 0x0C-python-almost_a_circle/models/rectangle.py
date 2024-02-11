#!/usr/bin/python3
"""models.rectangle"""
from models.base import Base


class Rectangle(Base):
    """Child class of Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiates attributes for class Rectangle

        Attributes:
            width - privates attr
            height - privates attr
            x - privates attr
            y - privates attr
            id - attr for parent class Base
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.integer_validator("x", x)
        self.integer_validator("y", y)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter property for attr width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter property for attr width
        """
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter property for attr height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter property for attr height
        """
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter property for attr x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter property for attr x
        """
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter property for attr y
        """
        return self.__y

    @width.setter
    def y(self, value):
        """Setter property for attr y
        """
        self.integer_validator("y", value)
        self.__y = value

    def integer_validator(self, name, value):
        """Validates an integer

        Raises:
            TypeError - if value is not an integer
            ValueError - if value is less than or equal to zero
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if (name == "width" or name == "height"):
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        if (name == "x" or name == "y"):
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Public method that returns the area value of the Rectangle instance
        """
        return (self.__width * self.__height)
