#!/usr/bin/python3
"""Check if an obj is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """Returns whether an obj is an exactly instance of a class or not
    """
    return (type(obj) == a_class)
