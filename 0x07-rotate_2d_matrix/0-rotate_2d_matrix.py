#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """ rotate_2d_matrix"""
    n = len(matrix)
    """
    for x in range(0, int(n / 2)):
        for y in range(x, n-1-x):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][n-1-x]
            matrix[y][n-1-x] = matrix[n-1-x][n-1-y]
            matrix[n-1-x][n-1-y] = matrix[n-1-y][x]
            matrix[n-1-y][x] = temp
    """
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
