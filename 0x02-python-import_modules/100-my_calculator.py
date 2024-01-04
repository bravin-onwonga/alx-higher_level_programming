#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
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
        res = add(a, b)

        print("{:d} {} {:d} = {:d}".format(a, op, b, res))

    elif (op == "-"):
        res = sub(a, b)

        print("{:d} {} {:d} = {:d}".format(a, op, b, res))

    elif (op == "*"):
        res = mul(a, b)

        print("{:d} {} {:d} = {:d}".format(a, op, b, res))

    elif (op == "-"):
        res = div(a, b)

        print("{:d} {} {:d} = {:d}".format(a, op, b, res))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
