#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    len_my_list = len(my_list)

    for i in range(len_my_list):
        new_list[i] = my_list[i]

    new_list = replace_in_list(new_list, idx, element)
    return new_list

