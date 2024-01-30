#!/usr/bin/python3
"""
Print out a full name
"""


def say_my_name(first_name, last_name=""):
    """
    Raises:
        TypeError: First name or last name are not string
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print('My name is ' + first_name + ' ' + last_name)
