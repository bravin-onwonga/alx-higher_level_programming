#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        last_idx = len(my_list) - 1

        while (last_idx >= 0):
            print("{:d}".format(my_list[last_idx]))
            last_idx -= 1
