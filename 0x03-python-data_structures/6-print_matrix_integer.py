#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format([i][j]), end=" ")

if __name__ == "__main__":
    print_matrix_integer()
