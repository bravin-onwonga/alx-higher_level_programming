#!/usr/bin/python3
"""
Returns an object for a json string"""
import json


def from_json_string(my_str):
    """Uses json to convert a string representation to its object

    Parameters:
        str to deserialize
    Returns:
        object
    """
    return json.loads(my_str)
