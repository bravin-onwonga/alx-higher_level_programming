#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

arg_list = sys.argv
arg_len = len(arg_list)

if (arg_len != 4):
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

a = int(arg_list[1])
b = int(arg_list[3])
op = arg_list[2]

if (op == "+"):
    if __name__ == "__main__":
        res = add(a, b)

        print("{:d} + {:d} = {:d}".format(a, b, res))

elif (op == "-"):
    if __name__ == "__main__":
        res = sub(a, b)

        print("{:d} - {:d} = {:d}".format(a, b, res))

elif (op == "*"):
    if __name__ == "__main__":
        res = mul(a, b)

        print("{:d} * {:d} = {:d}".format(a, b, res))

elif (op == "-"):
    if __name__ == "__main__":
        res = div(a, b)

        print("{:d} / {:d} = {:d}".format(a, b, res))

else:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
