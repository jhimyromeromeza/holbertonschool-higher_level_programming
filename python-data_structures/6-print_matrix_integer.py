#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        array = ""
        for j in i:
            array += str(j) + " "
        print(array.strip())
