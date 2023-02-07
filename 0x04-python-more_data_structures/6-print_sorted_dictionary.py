#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    a_dictionary = sorted(a_dictionary)

    for i in a_dictionary:
        print(i, a_dictionary[i])
