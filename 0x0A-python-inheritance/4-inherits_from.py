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
    return (type(obj).__name__ == type(a_class).__name__)
