#!/usr/bin/python3
"""
solve the problem of pascal_triangle
"""


def pascal_triangle(n):
    """
    calculate the pascal triangle
    by calculating the sum of two pervious variable to get the value
    of a variable in the next list and also add 1 to each side of the list
    """
    main_list = []

    if n > 0:
        for row in range(0, n):
            internal_list = []

            if row != 0:
                internal_list.append(1)
                for j in range(1, row):
                    internal_list.append(
                            main_list[row-1][j-1] + main_list[row-1][j])

            internal_list.append(1)
            main_list.append(internal_list)

    return main_list
