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


    if not m_a:
        raise TypeError("m_a can't be empty")
    if not m_b:
        raise TypeError("m_b can't be empty")
    for row in m_a:
        if len(row) == 0:
            raise TypeError("m_a can't be empty")
    for row in m_a:
        if len(row) == 0:
            raise TypeError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) and row for row in m_a):
        raise TypeError("m_a can't be empty")
    if not all(isinstance(row, list) and row for row in m_b):
        raise TypeError("m_b can't be empty")

    num_col_m_a = handle_m_a_if_matrix(m_a)

    num_row_m_b = handle_m_b_if_matrix(m_b)

    if (num_col_m_a != num_row_m_b):
        raise ValueError("m_a and m_b can't be multiplied")

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
