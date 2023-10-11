#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_m = []

    for i in matrix:
        tmp = []
        for j in i:
            tmp.append(j ** 2)
        new_m.append(tmp)
    return new_m
