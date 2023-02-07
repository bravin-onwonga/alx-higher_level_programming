#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    unique_list = {}
    
    for i in my_list:
        unique_list.append(i)

    for i in unique_list:
        sum = sum + i

    return sum
