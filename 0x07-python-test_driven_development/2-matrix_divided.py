#!/usr/bin/python3
"""
A function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    A function that divides all elements of a matrix.

    Args:
        matrix (_type_): _description_
        div (_type_): _description_
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0: