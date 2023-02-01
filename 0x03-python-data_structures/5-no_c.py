#!/usr/bin/python3

def no_c(my_string):
    new_str = ""
    len_str = len(my_string)

    for i in range(len_str):
        if my_string[i] == "c" or my_string[i] == "C":
            new_str = new_str.join("")
        else:
            new_str = new_str.join(my_string[i])
    print(new_str)
    print(my_string)


if __name__ == "__main__":
    no_c()
