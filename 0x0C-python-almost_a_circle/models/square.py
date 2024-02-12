#!/usr/bin/python3
"""models.square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square inherits from class rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates the square instance without creating new attributes

        Parameters:
            size - size attr
            x - attribute
            y - attribute
            id - id of instance
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """Overrides the str method in parent class"""
        s_id = self.id
        s_x = self.x
        s_y = self.y
        s_w = self.size
        return "[Square] ({}) {}/{} - {}".format(s_id, s_x, s_y, s_w)

    @property
    def size(self):
        """Getter for size attr"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size

        Parameters:
            value - value of size of square instance
        """
        super().integer_validator("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the values of the rectangle instance

        Parameter:
            args - variable number of attr in a tuple
            kwargs - variable number of attr with a key, value pair
        """
        if (len(args) > 0):
            len_args = len(args)
            if len_args == 1:
                super().update(id=args[0])
            if len_args == 2:
                super().update(id=args[0], width=args[1], height=args[1])
            if len_args == 3:
                val = args[1]
                super().update(id=args[0], width=val, height=val, x=args[2])
            if len_args == 4:
                val = args[1]
                v_id = args[0]
                v_x = args[2]
                v_y = args[3]
                super().update(id=v_id, width=val, height=val, x=v_x, y=v_y)

        elif kwargs:
            for k in kwargs:
                if k == "id":
                    super().update(id=kwargs[k])
                elif k == "size":
                    super().update(width=kwargs[k], height=kwargs[k])
                elif k == "x":
                    super().update(x=kwargs[k])
                elif k == "y":
                    super().update(y=kwargs[k])

    def to_dictionary(self):
        """Returns the dictionary representation of an instance of Square"""
        return ({'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y})
