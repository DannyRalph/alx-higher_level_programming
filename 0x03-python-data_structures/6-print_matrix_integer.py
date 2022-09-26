#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    new = []
    for i in matrix:
        for x in i:
            print("{:d}".format(x), end=" ")
        print("")
