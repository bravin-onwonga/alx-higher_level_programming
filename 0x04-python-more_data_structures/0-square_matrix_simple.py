#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_squared = []

    for r in matrix:
        a = []
        for c in r:
            a.append(c ** 2)
        matrix_squared.append(a)
        
    return matrix_squared
