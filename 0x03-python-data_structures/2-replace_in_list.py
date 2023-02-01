#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    len_my_list = len(my_list) - 1

    if idx > len_my_list or idx < 0:
        return my_list
    else:
        my_list[idx] = element
        return my_list


if __name__ == "__main__":
    replace_in_list()
