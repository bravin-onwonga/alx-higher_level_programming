#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    a_dictionary = sorted(a_dictionary)

    len_dict = len(a_dictionary)
    for i in len_dict:
        print(a_dictionary[i])
