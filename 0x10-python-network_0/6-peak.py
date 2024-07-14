#!/usr/bin/python3

"""
This module contains a function to find the peak element in a list of integers.
"""

def find_peak(list_of_integers):
    """
    Find a peak element in a list of integers.

    Args:
        list_of_integers (list): A list of integers.

    Returns:
        int: The peak element in the list.

    Examples:
        >>> find_peak([1, 2, 3, 4, 5])
        5
        >>> find_peak([5, 4, 3, 2, 1])
        5
        >>> find_peak([1, 3, 2, 4, 5])
        3
    """
    if not list_of_integers:
        return None
    low = 0
    high = len(list_of_integers) - 1
    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1
    return list_of_integers[low]
