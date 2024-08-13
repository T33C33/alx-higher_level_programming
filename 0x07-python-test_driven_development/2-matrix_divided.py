#!/usr/bin/python3
"""
A function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    A function that divides all elements of a matrix.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int/float): The divisor.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.

    Returns:
        list: A new matrix with each element divided by div.

    Examples:
        >>> matrix_divided([[3, 9], [12, 15]], -3)
        [[-1.0, -3.0], [-4.0, -5.0]]
    """

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise ValueError("matrix can't be empty")
    
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Create a new matrix with divided elements
    new_lst = [[round(element / div, 2) for element in row] for row in matrix]
    return new_lst
