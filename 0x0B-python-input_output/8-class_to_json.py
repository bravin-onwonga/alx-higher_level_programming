#!/usr/bin/python3
"""My class values
"""


def class_to_json(obj):
    """Returns a dictionary containing class Atrributes and their values"""
    my_dict = {}
    my_keys = [i for i in obj.__dict__.keys()]
    my_values = [i for i in obj.__dict__.values()]

    for key, value in zip(my_keys, my_values):
        my_dict[key] = value

    return my_dict
