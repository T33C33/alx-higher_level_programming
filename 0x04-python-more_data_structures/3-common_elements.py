'''
#!/usr/bin/python3
def common_elements(set_1, set_2):
    result = {}
    for first in set_1:
        for second in set_2:
            if first == second:
                result = first
    return result
This only returns single individual characters
'''


#!/usr/bin/python3
def common_elements(set_1, set_2):
    Result = set_1 & set_2
    return Result
