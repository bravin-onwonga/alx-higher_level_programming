#!/usr/bin/python3
"""
Simple function that adds two integers
Returns:
    sum of a and b
"""
def add_integer(a, b=98):
    """Simple function that adds two integers
    Raises:
        TypeError - if a or b is not an integer"""

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
