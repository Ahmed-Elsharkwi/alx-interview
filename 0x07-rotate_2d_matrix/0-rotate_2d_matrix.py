#!/usr/bin/python3
""" rotate 2d matrix
"""


def rotate_2d_matrix(matrix):
    """ rotate 2d matrix """
    rows = len(matrix)
    columns = len(matrix[0])

    if rows != columns:
        matrix.append([None] * rows)
        rows += 1

    for column in range(0, columns):
        for row in range(column, rows):
            if row != column:
                temp = matrix[row][column]
                matrix[row][column] = matrix[column][row]
                matrix[column][row] = temp
                if matrix[column][row] is None:
                    del matrix[column][row]

    length = len(matrix[0])
    for list_1 in matrix:
        right = length - 1
        left = 0
        while left < length / 2:
            temp = list_1[right]
            list_1[right] = list_1[left]
            list_1[left] = temp
            left += 1
            right -= 1
