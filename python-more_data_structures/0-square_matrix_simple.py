#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_lista = []
        for j in i:
            new_lista.append(j**2)
        new_matrix.append(new_lista)
    return new_matrix
