#!/usr/bin/python3
def no_c(my_string):
    list_str = [c for c in my_string if c not in "cC"]
    return "".join(list_str)
