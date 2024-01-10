#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    new_list = sorted(a_dictionary)

    for s in new_list:
        print("{} : {}".format(s, a_dictionary[s]))
