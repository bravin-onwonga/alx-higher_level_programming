#!/usr/bin/python3
def print_list_integer(my_list=[]):
    len_lst = len(my_list)
    i = 0

    while (i < len_lst):
        print("{}".format(my_list[i]))
        i += 1
