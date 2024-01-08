#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (matrix == [[]]):
        print()

    for row in matrix:
        len_row = len(row)
        for i in range(len_row):
            if (i != len_row - 1):
                print("{:d}".format(row[i]), end=" ")
            else:
                print("{:d}".format(row[i]))
