#!/usr/bin/python3
def max_integer(my_list=[]):
    len_lst = len(my_list)

    if len == 0:
        return None
    else:
        my_list.sort()
        return (my_list[len_lst - 1])

