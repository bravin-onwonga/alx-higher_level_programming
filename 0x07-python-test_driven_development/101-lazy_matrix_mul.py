#!/usr/bin/python3
"""
Module to multiply two matrices using numpy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
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
        raise TypeError("m_a shouldn't be empty")
    if not m_b:
        raise TypeError("m_b shouldn't be empty")
    for row in m_a:
        if len(row) == 0:
            raise TypeError("m_a shouldn't be empty")
    for row in m_a:
        if len(row) == 0:
            raise TypeError("m_b shouldn't be empty")

    if not isinstance(m_a, list):
        raise TypeError("type m_a should be list")
    if not isinstance(m_b, list):
         raise TypeError("type m_b should be list")
    if not all(isinstance(row, list) and row for row in m_a):
        raise TypeError("m_a shouldn't be empty")
    if not all(isinstance(row, list) and row for row in m_b):
        raise TypeError("m_b shouldn't be empty")


    num_col_m_a = 0
    num_row_m_b = 0

    if type(m_a[0]) is list:
        num_col_m_a = handle_m_a_if_matrix(m_a)
    else:
        for n in m_a:
            if type(n) not in [int, float]:
                raise TypeError("values in m_a should be of type integers or floats")
            num_col_m_a += 1

    if type(m_b[0]) is list:
        num_row_m_b = handle_m_b_if_matrix(m_b)
    else:
        for n in m_b:
            if type(n) not in [int, float]:
                raise TypeError("values in m_b should be of type integers or floats")
        num_row_m_b += 1

    if (num_col_m_a != num_row_m_b):
        raise ValueError("m_a columns don't match number of m_b rows")

    new_matrix = np.dot(m_a, m_b)

    return (new_matrix)


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
            raise TypeError('rows of m_a must be of the same size')
        for n in row:
            if type(n) not in [int, float]:
                raise TypeError("values in m_a should be of type integers or floats")
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
            raise TypeError('rows of m_b must be of the same size')
        for n in row:
            if type(n) not in [int, float]:
                raise TypeError("values in m_b should be of type integers or floats")
        num_row_matrix += 1
    return (num_row_matrix)
