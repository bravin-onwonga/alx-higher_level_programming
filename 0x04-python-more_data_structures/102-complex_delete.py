#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    my_list = []
    for x, y in enumerate(a_dictionary):
        if y == value:
            my_list.append(x)

    i = 0
    while (my_list[i]):
        del a_dictionary[my_list[i]]
        i += 1

    return (a_dictionary)
