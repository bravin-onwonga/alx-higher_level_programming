#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    my_list = []
    for x in a_dictionary:
        if a_dictionary[x] == value:
            my_list.append(x)

    i = 0
    len_list = len(my_list)
    while (i < len_list):
        del a_dictionary[my_list[i]]
        i += 1

    return (a_dictionary)
