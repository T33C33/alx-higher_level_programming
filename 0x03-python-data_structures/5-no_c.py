#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for char in my_string:
        if char.lower() != 'c' or char.upper() != 'C':
            result += char
    return result
