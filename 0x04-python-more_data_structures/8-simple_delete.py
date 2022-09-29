#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    k = list(a_dictionary)
    for i in k:
        if i == key:
            del a_dictionary[key]
    return (a_dictionary)
