#!/usr/bin/python3
def uniq_add(my_list=[]):

    unique_integers = set()
    result = 0
    for num in my_list:
        unique_integers.add(num)
        result = sum(unique_integers)

    return result
