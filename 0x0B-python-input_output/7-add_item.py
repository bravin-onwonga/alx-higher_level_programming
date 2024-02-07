#!/usr/bin/python3
"""Append data to a file, creates one if it doesn't exist"""
import sys
import json


def add_items_to_json():
    """Creates file if it doesn't exist
    Reads from file if it exist, file should contain a list
    Appends args passed form command line to the list

    Exceptions:
        Ignores the FileNotFoundError and creates file
    """
    new_list = []
    num_args = len(sys.argv)

    for i in range(1, num_args):
        new_list.append(sys.argv[i])

    my_list = []

    try:
        with open("add_item.json", 'r+', encoding="utf-8") as my_file:
            my_file.seek(0)
            txt = my_file.read()

        if txt:
            my_list = [i for i in json.loads(txt)]

    except FileNotFoundError:
        pass

    new_list = my_list + new_list

    with open("add_item.json", 'w', encoding="utf-8") as my_file:
        content = json.dumps(new_list)
        my_file.write(content)


if __name__ == "__main__":
    add_items_to_json()
