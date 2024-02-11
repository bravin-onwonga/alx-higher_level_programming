#!/usr/bin/python3
"""Module models.base"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiates attribute for objects

        Attribute:
            id - integer attribute for id of object
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
