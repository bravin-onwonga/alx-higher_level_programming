#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    len_my_list = len(my_list)

    for i in range(len_my_list):
        new_list.append(my_list[i])

    if (idx < 0 or idx >= len_my_list):
        pass
    else:
        new_list[idx] = element
    return new_list
