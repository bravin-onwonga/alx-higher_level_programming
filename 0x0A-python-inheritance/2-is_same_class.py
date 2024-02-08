#!/usr/bin/python3
"""Check if an obj is an instance of a class
"""


def is_same_class(obj, a_class):
    """Returns whether an obj is an instance of a class or not
    """
    return (type(obj) == a_class)
