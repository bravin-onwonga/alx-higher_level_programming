#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""

    str_len = len(str)
    i = 0
    while (i < str_len):
        if (i != n):
            new_str += str[i]
        i += 1
    return (new_str)
