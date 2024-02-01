#!/usr/bin/python3
"""The N queens puzzle
"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

if not isinstance(N, int):
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(4)


def solve_puzzle(N):
    """solves the N queens problem"""
    new_matrix = []
    for i in range(N):
        for n in range(N):
            new_matrix.append[i, n]
        print(new_matrix)
        new_matrix = []
