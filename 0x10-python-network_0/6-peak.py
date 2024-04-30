#!/usr/bin/python3
"""
Finds the largest number in a list and must have the lowest complexity
"""

if __name__ == "__main__":
    def find_peak(list_of_integers):
        lst = list_of_integers
        len_lst = len(lst)
        if (len_lst == 0):
            return None
        if (len_lst == 1):
            return (lst[0])
        else:
            pivot = lst[0]
            sort_list()
