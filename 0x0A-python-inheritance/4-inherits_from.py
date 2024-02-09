#!/usr/bin/python3
"""Checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """Returns True is an object inherited from a class; otherwise False

    Parameters:
        obj - object
        a_class - class info
    """
    if (type(obj) is int and a_class is int):
        return False
    return issubclass(obj.__class__, a_class)
