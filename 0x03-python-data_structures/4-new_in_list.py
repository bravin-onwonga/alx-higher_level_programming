#!/usr/bin/python3

def _cpy_list(my_list):
    len_list = len(my_list)
    list_copy = []

    for i in range(len_list):
        list_copy.append(my_list[i])

    return list_copy


def new_in_list(my_list, idx, element):
    len_my_list = len(my_list) - 1

    if idx > len_my_list:
        _cpy_list(my_list)
    elif idx < 0:
        _cpy_list(my_list)
    else:
        new_list = _cpy_list(my_list)
        new_list[idx] = element
        return new_list
    return my_list
        

if __name__ == "__main__":
    new_in_list()
