#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for index, value in a_dictionary.items():
        new_dict[index] = value * 2
    return new_dict
