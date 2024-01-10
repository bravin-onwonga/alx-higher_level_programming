#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = {}
    new_list = sorted(a_dictionary)

    for key in new_list:
        value = a_dictionary[key]
        new_dict[key] = value * 2

    return new_dict