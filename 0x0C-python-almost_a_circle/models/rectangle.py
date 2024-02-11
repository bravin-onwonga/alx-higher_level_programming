#!/usr/bin/python3
"""models.rectangle"""
from models.base import Base


class Rectangle(Base):
    """Child class of Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instatiates attributes for class Rectangle

        Attributes:
            width - privates attr
            height - privates attr
            x - privates attr
            y - privates attr
            id - attr for parent class Base
        """
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
        self.__y = value
