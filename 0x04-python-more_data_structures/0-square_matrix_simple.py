#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_squared = []

    for r in matrix:
        for c in r:
            matrix_squared.append(c ** 2)
        
    return matrix_squared
