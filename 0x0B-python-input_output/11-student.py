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

    def get_attributes(self):
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
            return self.get_attributes()
        else:
            new_dict = self.to_json()
            my_dict = {}
            for key in new_dict:
                if key in attrs:
                    my_dict[key] = new_dict[key]
        return my_dict

    def reload_from_json(self, json):
        """Defines a new instance values based on values from a file"""
        for k in json:
            if k == "first_name":
                self.first_name = json[k]
            if k == "last_name":
                self.last_name = json[k]
            if k == "age":
                self.age = json[k]
