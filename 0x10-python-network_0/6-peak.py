#!/usr/bin/python3

"""
This module provides a function to find a peak element in a list of integers using a recursive binary search algorithm.
"""

def find_peak(list_of_integers):
    """
    Finds a peak element in a list of integers using a recursive binary search algorithm.

    Args:
        list_of_integers (list): The list of integers to search for a peak.

    Returns:
        int: The peak element in the list, or None if the list is empty.
    """

    if not list_of_integers:
        return None

    def find_peak_util(nums, low, high):
        mid = (low + high) // 2
        
        """is mid peak?"""
        if (mid == 0 or nums[mid] >= nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] >= nums[mid + 1]):
            return nums[mid]
        
        """if mid is not peak and element on left is greater than mid, then peak is on left"""
        if mid > 0 and nums[mid - 1] > nums[mid]:
            return find_peak_util(nums, low, mid - 1)
        
        """if mid is not peak and element on right is greater than mid, then peak is on right"""
        return find_peak_util(nums, mid + 1, high)

    return find_peak_util(list_of_integers, 0, len(list_of_integers) - 1)
