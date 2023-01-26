#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len = len(argv)
    i  = 1
    ans = 0

    while(i < len):
        ans = ans + int(argv[i])
        i += 1
    print("{}".format(ans))
