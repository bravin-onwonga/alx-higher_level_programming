#!/usr/bin/python3
from add_0 import add

if __name__ == "__main__":
    a = 1
    b = 2
    add(a, b)

    res = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, res))
