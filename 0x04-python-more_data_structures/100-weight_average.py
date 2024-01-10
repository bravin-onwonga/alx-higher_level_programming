#!/usr/bin/python3
def weight_average(my_list=[]):
    len_list = len(my_list)

    ttl_weight = 0
    divisor = 0

    for i in range (len_list):
        ttl_weight += my_list[i][0] * my_list[i][1]
        divisor += my_list[i][1]

    return ttl_weight / divisor
