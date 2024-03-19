#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        formated_row = []
        for ele in row:
            formated_row.append('{:d}'.format(ele))
        print(' '.join(formated_row))
