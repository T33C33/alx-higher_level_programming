#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    result = set_1 | set_2
    sorted_result = sorted(result)
    return sorted_result