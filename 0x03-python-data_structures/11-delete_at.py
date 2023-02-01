#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if my_list == []:
        return my_list
    else:
        len_lst = len(my_list) - 1

        if idx > len_lst or idx < 0:
            return my_list

        else:
            del my_list[idx]
            return my_list
