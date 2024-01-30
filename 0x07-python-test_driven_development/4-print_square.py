#!/usr/bin/python3
def print_square(size):
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
