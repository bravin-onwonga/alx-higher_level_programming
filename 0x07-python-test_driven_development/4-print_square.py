#!/usr/bin/python3
"""
Prints a square
"""
def print_square(size):
    """
    Raises:
        TypeError: size is not and integer
        ValueError: size is less than zero
    """
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')
    elif type(size) is float and size > 0:
        size = int(size)

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    if (size == 0):
        print()

    for n in range(size):
        print("#" * size)
