#!/usr/bin/python3
"""Defining a function pascal_triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascals triangle of number"""
    row = []
    pastriangle = [[1]]

    if n <= 0:
        return []

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(pastriangle[i - 1][j - 1] + pastriangle[i - 1][j])

        row.append(1)
        pastriangle.append(row)

    return pastriangle
