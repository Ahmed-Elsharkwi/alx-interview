#!/usr/bin/python3
"""
n queens problem
"""
import sys


def check(row, column, check_list, n):
    """
    check if there is any another queen in the column and right and left
    digional of the added queen
    """

    prev_row = row - 1
    next_column = column + 1
    prev_column = column - 1

    while prev_row >= 0:
        if [prev_row, column] in check_list:
            return False
        prev_row -= 1

    prev_row = row - 1
    while next_column < n and prev_row >= 0:
        if [prev_row, next_column] in check_list:
            return False
        next_column += 1
        prev_row -= 1

    prev_row = row - 1
    while prev_column >= 0 and prev_row >= 0:
        if [prev_row, prev_column] in check_list:
            return False
        prev_column -= 1
        prev_row -= 1

    return True


def nqeen(check_list, row, column, n):
    """ nqeen function """
    res = True

    if row == n:
        return True

    for i in range(0, n):

        if row == 0:
            res = True
            check_list = []
        check_list.append([row, i])

        if row != 0:
            res = check(row, i, check_list, n)
            if res is False:
                del check_list[-1]

        if res is True:
            res = nqeen(check_list, row + 1, i, n)

            if res is not False:
                print(check_list)

            del check_list[-1]

    return False


def main():
    """ main function """
    if len(sys.argv) != 2:
        print(f"Usage: nqueens N")
        exit(1)

    if sys.argv[1].isdigit() is False:
        print(f"N must be a number")
        exit(1)

    if int(sys.argv[1]) < 4:
        print(f"N must be at least 4")
        exit(1)

    over_list = []
    nqeen("", 0, 0, int(sys.argv[1]))


main()
