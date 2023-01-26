#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculating_1 import add, sub, mul, div

    len = len(argv) - 1

    if len < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[1] != "+" or "-" or "*" or "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        n1 = int(agrv[0])
        n2 = int(argv[2])
        op = argv[1]
        if op == "+":
            print("{} {} {} = {}".format(n1, op, n2, calculating_1.add(n1, n2)))
        elif op == "-":
            print("{} {} {} = {}".format(n1, op, n2, sub(n1, n2)))
        elif op == "*":
            print("{} {} {} = {}".format(n1, op, n2, mul(n1, n2)))
        else:
            print("{} {} {} = {}".format(n1, op, n2, div(n1, n2)))
