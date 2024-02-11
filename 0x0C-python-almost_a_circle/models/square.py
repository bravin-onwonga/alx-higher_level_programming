#!/usr/bin/python3
"""models.square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square inherits from class rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates the square instance without creating new attributes
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overrides the str method in parent class"""
        s_id = self.id
        s_x = self.x
        s_y = self.y
        s_w = self.width
        return "[Square] ({}) {}/{} - {}".format(s_id, s_x, s_y, s_w)
