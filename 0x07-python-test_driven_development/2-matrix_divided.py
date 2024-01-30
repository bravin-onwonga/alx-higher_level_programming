#!/usr/bin/python3
"""
A function that divides all items in a matrix
Returns:
    A new matrix with the new values
"""
def matrix_divided(matrix, div):
    """Divides all items in a matrix by a divisor(div)
    Raises:
        ZeroDivisionError: if div is zero
        TypeError: div is not int and not float
                   rows of matrix are of varying length
                   values type in matrix are not int and not float
    """
    new_matrix = []
    if div == 0:
        raise ZeroDivisionError('division by zero')

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')

    l = len(matrix[0])

    for row in matrix:
        if len(row) != l:
            raise TypeError('Each row of the matrix must have the same size')
        for n in row:
            if not isinstance(n, int) and not isinstance(n, float):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    for row in matrix:
        temp_list = []
        for n in row:
            res = n / div
            temp_list.append(round(res, 2))
        new_matrix.append(temp_list)

    return new_matrix
