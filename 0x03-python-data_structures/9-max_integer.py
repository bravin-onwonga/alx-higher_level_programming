#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None

    else:
        len_lst = len(my_list)

        for i in range(len_lst):
            if my_list[i] > my_list[i + 1]:
                tmp = my_list[i + 1]
                my_list[i + 1] = my_list[i]
                my_list[i] = tmp
        return my_list[i]
