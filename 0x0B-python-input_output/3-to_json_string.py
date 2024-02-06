#!/usr/bin/python3
"""
Returns a json rep of an object"""
import json


def to_json_string(my_obj):
    """Uses json to convert a object to its string representation

    Parameters:
        object to serialize
    Returns:
        str rep of object
    """
    return json.dumps(my_obj)
