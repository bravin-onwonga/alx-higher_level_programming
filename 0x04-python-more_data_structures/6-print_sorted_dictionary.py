#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    a_dictionary = sorted(a_dictionary)

    for item in a_dictionary:
        print(item, a_dictionary[item])
