#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    x = matrix.copy()
    for i in range(len(matrix)):
        x[i] = list(map(lambda y: y**2, matrix[i]))
        return x
