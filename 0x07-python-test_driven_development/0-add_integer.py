#!/usr/bin/python3
"""
module contains an addition function
"""


def add_integer(a, b=98):
    """
    This function adds two integers together

    Args:
        a (_type_): _description_
        b (int, optional): _description_. Defaults to 98.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
