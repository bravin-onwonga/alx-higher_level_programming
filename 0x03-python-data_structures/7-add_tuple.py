#!/usr/bin/python3

idef add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    list_sum = []
    for i, j in zip(list_a, list_b):
        list_sum.append(i + j)
    tuple_sum = tuple(list_sum)
    return tuple_c
