#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        for i in a_dictionary:
            if max(zip(a_dictionary.values(), a_dictionary.keys()))[1]:
                maximum = max(zip(a_dictionary.values(), a_dictionary.keys()))[1]
                return (maximum)
            else:
                return (None)
