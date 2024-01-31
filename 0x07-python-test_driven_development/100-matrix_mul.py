#!/usr/bin/python3
"""Module to multiply two matrices
"""


def matrix_mul(m_a, m_b):
    """Function to return a multiple of two matrices
    Raises:
        TypeError: if type(m_a) or type(m_b) are not list
                   if m_a or m_b are empty
                   if values in neither lists is not int or float
                   if length of list in matrices vary
        ValueError: if matrices can't be multiplied
    """
    new_matrix = []

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if len(m_a) == 0:
        raise TypeError("m_a can't be empty")
    if len(m_b) == 0:
        raise TypeError("m_b can't be empty")
    if type(m_a[0]) is list and len(m_a) == 1:
        raise TypeError("m_a can't be empty")
    if type(m_b[0]) is list and len(m_b) == 1:
        raise TypeError("m_b can't be empty")

    num_col_m_a = 0
    num_row_m_b = 0

    if type(m_a[0]) is list:
        num_col_m_a = handle_m_a_if_matrix(m_a)
    else:
        for n in m_a:
            if type(n) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
            num_col_m_a += 1

    if type(m_b[0]) is list:
        num_row_m_b= handle_m_b_if_matrix(m_b)
    else:
        for n in m_b:
            if type(n) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
        num_row_m_b += 1

    if (num_col_m_a != num_row_m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    if num_col_m_a == 1:
        mul = m_a[0]
        for n in m_b:
            new_matrix.append(n * mul)
    elif type(m_a[0]) is not list:
        len_m_a = len(m_a)
        i = 0
        while i < len_m_a:
            j = 0
            value = 0
            while j < len_m_a:
                value += m_a[j] * m_b[j][i]
                j += 1
            new_matrix.append(value)
            i += 1

    else:
        num_rows = 0
        for _ in m_a:
            num_rows += 1
        i = 0
        while (i < num_rows):
            temp_list = []
            k = 0
            j = 0
            value = 0
            while (j < num_row_m_b):
                value += m_a[i][j] * m_b[j][k]
                j += 1
                if (j == num_row_m_b):
                    j = 0
                    k += 1
                    temp_list.append(value)
                    value = 0
                if (k == len(m_b[0])):
                    break
            i += 1
            new_matrix.append(temp_list)

    return new_matrix


def handle_m_a_if_matrix(m_a):
    """Function to handle case for m_a being a matrice
    Raises:
        TypeError: list of varying length
                    values are not of type int or float
    """
    len_row = len(m_a[0])
    num_col_matrix = 0

    for row in m_a:
        if len(row) != len_row:
            raise TypeError('each row of m_a must be of the same size')
        for n in row:
            if type(n) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
            num_col_matrix += 1

    return (num_col_matrix / len(m_a))

def handle_m_b_if_matrix(m_b):
    """Function to handle case for m_b being a matrice
    Raises:
        TypeError: list of varying length
                    values are not of type int or float
    """
    len_row = len(m_b[0])
    num_row_matrix = 0

    for row in m_b:
        if len(row) != len_row:
            raise TypeError('each row of m_b must be of the same size')
        for n in row:
            if type(n) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
        num_row_matrix += 1
    return (num_row_matrix)
