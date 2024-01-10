#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    new_list = sorted(a_dictionary)
    value_list = []

    for key in new_list:
        value_list.append(a_dictionary[key])

    value_list.sort(reverse=True)

    for key in new_list:
        if a_dictionary[key] == value_list[0]:
            return key
