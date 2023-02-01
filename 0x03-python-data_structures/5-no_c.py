#!/usr/bin/python3

def no_c(my_string):
    new_str = ""
    len_str = len(my_string)

    for i in range(len_str):
        if my_string[i] == "c" or my_string[i] == "C":
            my_string[i] = ""
        new_str = new_str.join(my_string[i])
    return new_str


if __name__ == "__main__":
    no_c()
