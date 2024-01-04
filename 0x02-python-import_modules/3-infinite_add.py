#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_list = sys.argv
    arg_len = len(arg_list)

    if arg_len == 1:
        print("0")
    elif arg_len == 2:
        print("{}".format(arg_list[1]))
    else:
        sum = 0
        for i in range(1, arg_len):
            sum += int(arg_list[i])
        print("{}".format(sum))
