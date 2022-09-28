#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    return ([list(map((lambda x: x * x), i)) for i in new_matrix])
