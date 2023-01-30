#!/usr/bin/python3

def element_at(my_list, idx):
    len_list = len(my_list) - 1

    if len_list > idx or idx < 0:
        return None

    print("{}".format(my_list[idx]))


if __name__ == "__main__":
    element_at()
