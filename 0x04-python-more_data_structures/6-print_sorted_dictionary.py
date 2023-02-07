#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    a_dictionary = sorted(a_dictionary)

    for k, v in a_dictionary.items():
        print(k, v)
