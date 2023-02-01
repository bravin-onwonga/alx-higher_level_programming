#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    for i, j in zip(tuple_a, tuple_b):
        tuple_c = tuple_c + (i + j)
    return tuple_c
