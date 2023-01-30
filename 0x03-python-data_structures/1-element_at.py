#!/usr/bin/python3

def element_at(my_list, idx):
    len_list = len(my_list) - 1

    if idx > len_list or idx < 0:
        return None
    else:
        print("Element at index {} is {}".format(idx, my_list[idx]))


if __name__ == "__main__":
    element_at()
