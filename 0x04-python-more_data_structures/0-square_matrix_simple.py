#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_squared = []

    for i in len(matrix):
        a = []

        for j in len(i):
            a.append((matrix[i][j]) ** 2))
            
        matrix_squared.append(a)
        return matrix_squared
