#!/usr/bin/python3
"""Function to print the pascal triangle
"""


def pascal_triangle(n):
    """Creates a matrix containing lists with values of the pascal triangle

    Parameters:
        n - level of the pascal triangle to print

    Returns:
        matrix
    """

    matrix = []
    if n <= 0:
        return matrix

    temp_list = [1]
    matrix.append(temp_list)

    if n == 1:
        return matrix

    if n == 2:
        matrix.append([1, 1])
        return matrix

    matrix.append([1, 1])
    i = 1
    while i < (n - 1):
        temp_list = []
        ind = 0
        temp_list.append(1)
        len_lst = len(matrix[i])
        while (ind < len_lst):
            temp_list.append(matrix[i][ind] + matrix[i][ind + 1])
            ind += 1
            if ((ind + 1) == len_lst):
                temp_list.append(1)
                ind += 1
        matrix.append(temp_list)
        i += 1

    return (matrix)
