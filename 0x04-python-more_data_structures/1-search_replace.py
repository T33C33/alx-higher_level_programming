#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_ls = []

    for item in my_list:
        if item == search:
            new_ls.append(replace)
        else:
            new_ls.append(item)
    return new_ls
