#!/usr/bin/python3
from math import factorial


def pascal_triangle(n):
    """return a list of lists of integers representing
      the Pascal’s triangle of n
    """
    triangle = []
    for row in range(n):
        res = []
        for col in range(row + 1):
            result = factorial(row) // (factorial(col) * factorial(row - col))
            res.append(result)
        triangle.append(res)
    return triangle
