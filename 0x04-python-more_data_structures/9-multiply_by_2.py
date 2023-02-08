#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    for i in a_dictionary:
        value = a_dictionary[i]
        a_dictionary[i] = value * 2
    return a_dictionary
