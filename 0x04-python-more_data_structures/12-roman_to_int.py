#!/usr/bin/python3
def is_valid_roman_string(roman_string):
    if not isinstance(roman_string, str) or \
            not all(char in "IVXLCDM" for char in roman_string):
        return False
    return True


def roman_to_int(roman_string):
    def get_roman_value(roman_char):
        return {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}.get(roman_char, 0)

    if not is_valid_roman_string(roman_string):
        return 0

    result = 0
    prev_value = 0

    for numeral in reversed(roman_string):
        value = get_roman_value(numeral)
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result
