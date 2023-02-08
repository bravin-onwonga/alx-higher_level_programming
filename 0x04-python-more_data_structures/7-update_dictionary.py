#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    new_dict = {}

    for i in a_dictionary:
        new_dict[i] = a_dictionary[i]

    new_dict[key] = value
    print(new_dict)
