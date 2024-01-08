#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    last_index = len(my_list) - 1

    if (last_index < 0):
        print()

    while (last_index >= 0):
        print("{:d}".format(my_list[last_index]))
        last_index -= 1
