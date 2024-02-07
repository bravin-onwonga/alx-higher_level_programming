#!/usr/bin/python3
"""Creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Returns an object from a JSON File

    Parameters:
        filename: json file
    Returns:
        Object form json file
    """

    with open(filename, 'r') as my_file:
        for line in my_file:
            return json.loads(line)
