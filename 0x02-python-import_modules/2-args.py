#!/usr/bin/python3
import sys

if __name__ == "__main__":
	arg_list = sys.argv
	arg_len = len(arg_list)
	if arg_len == 1:
		print("0 arguments.")

	elif arg_len == 2:
		print("1 argument:")
		print("1: {}".format(arg_list[1]))

	else:
		print("{} arguments:".format(arg_len - 1))
		i = 1
		while (i < arg_len):
			print("{}: {}".format(i, arg_list[i]))
			i  += 1
