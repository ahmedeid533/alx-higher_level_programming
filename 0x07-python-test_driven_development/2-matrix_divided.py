#!/usr/bin/python3
"""divide example"""


def matrix_divided(matrix, div):
    """devide func"""

    mat_res = []
    mat_row = []
    massage = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(div, (int, float))):
        raise TypeError("div must be a number")
    elif (div == 0):
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError(massage)
    row_len = 0
    for matRow in matrix:
        if not isinstance(matRow, list):
            raise TypeError(massage)
        row_len = len(matrix[0])
        if len(matRow) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for item in matRow:
            if (not isinstance(item, (int, float))):
                raise TypeError(massage)
            mat_row.append(round((item / div), 2))
        mat_res.append(mat_row)
        mat_row = []
    return mat_res
