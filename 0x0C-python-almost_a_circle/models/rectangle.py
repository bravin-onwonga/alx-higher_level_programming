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

        Parameters:
            value - value of attr width
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

        Parameters:
            value - value of attr height
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

        Parameters:
            value - value of attr x
        """
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter property for attr y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter property for attr y

        Parameters:
            value - value of attr y
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

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        rect = ""

        for _ in range(self.__y):
            rect += '\n'
        i = 0
        while (i < self.__height):
            rect += " " * self.__x
            rect += "#" * self.__width
            if i != self.__height - 1:
                rect += '\n'
            i += 1
        print(rect)
        return rect

    def __str__(self):
        """Returns a customized string"""
        s_id = self.id
        s_x = self.__x
        s_y = self.__y
        s_w = self.__width
        s_h = self.__height
        s_R = "Rectangle"
        return "[{}] ({}) {}/{} - {}/{}".format(s_R, s_id, s_x, s_y, s_w, s_h)

    def update(self, *args, **kwargs):
        """Updates the values of the rectangle instance

        Parameter:
            args - variable number of attr in a tuple
            kwargs - variable number of attr with a key, value pair
        """
        if (len(args) > 0):
            len_args = len(args)
            if len_args == 1:
                self.id = args[0]
            if len_args == 2:
                self.id = args[0]
                self.integer_validator("width", args[1])
                self.__width = args[1]
            if len_args == 3:
                self.id = args[0]
                self.integer_validator("width", args[1])
                self.integer_validator("height", args[2])
                self.__width = args[1]
                self.__height = args[2]
            if len_args == 4:
                self.id = args[0]
                self.integer_validator("width", args[1])
                self.integer_validator("height", args[2])
                self.integer_validator("x", args[3])
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            if len_args == 5:
                self.id = args[0]
                self.integer_validator("width", args[1])
                self.integer_validator("height", args[2])
                self.integer_validator("x", args[3])
                self.integer_validator("y", args[4])
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]

        elif kwargs:
            for k in kwargs:
                if k == "id":
                    self.id = kwargs[k]
                if k == "width":
                    self.integer_validator("width", kwargs[k])
                    self.__width = kwargs[k]
                if k == "height":
                    self.integer_validator("height", kwargs[k])
                    self.__height = kwargs[k]
                if k == "x":
                    self.integer_validator("x", kwargs[k])
                    self.__x = kwargs[k]
                if k == "y":
                    self.integer_validator("y", kwargs[k])
                    self.__y = kwargs[k]

    def to_dictionary(self):
        """Returns the dictionary representation of an instance"""
        s_x = self.__x
        s_y = self.__y
        s_id = self.id
        s_h = self.__height
        s_w = self.__width
        return ({'x': s_x, 'y': s_y, 'id': s_id, 'height': s_h, 'width': s_w})
