#!/usr/bin/python3
"""
Writes json str to a file"""
import json


def save_to_json_file(my_obj, filename):
    """Uses json to convert an object to a string representation

    Parameters:
        my_obj: object to serialize and write
        filename: name of file to write to
    """
    txt = json.dumps(my_obj)

    with open(filename, 'w') as my_file:
        my_file.write(txt)
