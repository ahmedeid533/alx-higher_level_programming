#!/usr/bin/python3
"""pascal"""


def pascal_triangle(n):
    """pascal func"""
    if n <= 0:
        return []

    tri = [[1]]
    while len(tri) != n:
        tri = tri[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        tri.append(temp)
    return tri
