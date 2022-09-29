#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a = sorted(a_dictionary)
    new_dict = a_dictionary.copy()
    for i in a:
        new_dict[i] = a_dictionary[i] * 2
    return (new_dict)
