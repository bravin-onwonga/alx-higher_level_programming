#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    lst_len = 0
    count = 0

    for ele in my_list:
        len_lst += 1

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            print("")
            return len_lst
        count += 1
    print("")
    return count
