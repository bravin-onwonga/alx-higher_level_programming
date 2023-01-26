#!/usr/bin/python3

def calc():
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    n1 = int(argv[1])
    n2 = int(argv[3])
    op = argv[2]
    if op != "+" and  op != "-" and op != "*" and op != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if op == "+":
        print("{} {} {} = {}".format(n1, op, n2, add(n1, n2)))
    elif op == "-":
        print("{} {} {} = {}".format(n1, op, n2, sub(n1, n2)))
    elif op == "*":
        print("{} {} {} = {}".format(n1, op, n2, mul(n1, n2)))
    else:
        print("{} {} {} = {}".format(n1, op, n2, div(n1, n2)))

if __name__ == "__main__":
    calc()
