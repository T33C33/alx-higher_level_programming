#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        Biggest = max(a_dictionary, key=a_dictionary.get)
        return Biggest
    else:
        return None
