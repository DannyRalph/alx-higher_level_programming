#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i in a_dictionary.copy():
        if a_dictionary[i] == value:
            m = i
            del a_dictionary[m]
    return (a_dictionary)
