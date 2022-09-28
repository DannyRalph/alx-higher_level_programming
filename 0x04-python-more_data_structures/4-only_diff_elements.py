#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set1 = list(set_1 - set_2)
    set2 = list(set_2 - set_1)
    set_3 = set(set1 + set2)
    return (set_3)
