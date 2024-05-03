#!/usr/bin/python3
"""
Finds the largest number in a list and must have the lowest complexity
"""

def find_peak(list_of_integers):
    lst = list_of_integers
    len_lst = len(lst)
    if (len_lst == 0):
        return None
    if (len_lst == 1):
        return (lst[0])
    else:
        my_lst = quicksort(lst)
        peak = my_lst.pop()
        return (peak)


def quicksort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst.pop()

    lesser = []
    greater = []

    for x in lst:
        if x <= pivot:
            lesser.append(x)
        else:
            greater.append(x)

    return quicksort(lesser) + [pivot] + quicksort(greater)

if __name__ == "__main__":
    pass
