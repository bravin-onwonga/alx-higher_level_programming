#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_lst = []

    len_lst = len(my_list)
    for i in range(len_lst):
        if i % 2 == 0:
            new_lst.append(True)
        else:
            new_lst.append(False)
    return new_lst
