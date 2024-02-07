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
