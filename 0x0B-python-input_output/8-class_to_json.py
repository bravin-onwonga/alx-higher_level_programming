#!/usr/bin/python3
def class_to_json(obj):
    my_dict = {}
    my_keys = [i for i in obj.__dict__.keys() if i[:1] != '_']
    my_values = [i for i in obj.__dict__.values()]

    for key, value in zip(my_keys, my_values):
        my_dict[key] = value

    return my_dict
