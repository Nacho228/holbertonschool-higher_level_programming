#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    simple_square = []
    for y in matrix:
        y_square = []
        for i in y:
            i_square = i * i
            y_square.append(i_square)
        simple_square.append(y_square)
    return simple_square
