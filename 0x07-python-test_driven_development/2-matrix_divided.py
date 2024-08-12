#!/usr/bin/python3
"""
A function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    A function that divides all elements of a matrix.

    Args:
        matrix (_type_): represents a matrix
        div (_type_): represents a number to divide by
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix \
            (list of lists) of integers/floats")
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        for element in row:
            new_lst = [
                [round(element / div, 2) for element in row]
                for row in matrix]
            return new_lst
