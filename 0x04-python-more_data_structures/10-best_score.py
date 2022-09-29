#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        for i in a_dictionary:
            maximum = max(a_dictionary)
            return (maximum)
            if max(a_dictionary) == None:
                return (None)
    else:
        return (None)
