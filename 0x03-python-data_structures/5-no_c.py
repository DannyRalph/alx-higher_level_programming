#!/usr/bin/python3
def no_c(my_string):
    m = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        m += i
    return (m)
