#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            n = ord(c) - 32
        else:
            n = ord(c)
        print("{:c}".format(n), end="")
