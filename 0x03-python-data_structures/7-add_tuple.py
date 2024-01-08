#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_tuple_a = len(tuple_a)
    len_tuple_b = len(tuple_b)

    if len_tuple_a == 1:
        tuple_a = (tuple_a[0], 0)

    elif len_tuple_b == 1:
        tuple_b = (tuple_a[1], 0)

    elif len_tuple_a == 0:
        tuple_a = (0, 0)

    elif len_tuple_b == 0:
        tuple_b = (0, 0)

    a = tuple_a[0] + tuple_b[0]
    b = tuple_a[1] + tuple_b[1]

    return a, b
