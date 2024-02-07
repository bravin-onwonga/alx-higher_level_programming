#!/usr/bin/python3
"""Class that returns a dict of attributes and values
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Intiializes the calls

        Values:
            first_name - student first name
            last_name - student last name
            age - age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary containing class atrributes and their values"""
        my_dict = {}
        my_keys = [i for i in self.__dict__.keys()]
        my_values = [i for i in self.__dict__.values()]

        for key, value in zip(my_keys, my_values):
            my_dict[key] = value

        return my_dict

    def to_json(self, attrs=None):
        """Returns dictionary of attributes and values

        Attributes to return are in list attributes
        if not values are passed return all attributes
        """

        if attrs is None:
            return self.to_json()
        else:
            new_dict = self.to_json()
            for key in new_dict:
                if key not in attrs:
                    del new_dict[key]
        return new_dict
