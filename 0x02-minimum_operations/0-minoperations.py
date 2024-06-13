#!/usr/bin/python3
"""
calculate the number of the operations which will be taken
to reach the number of n which is the number of letter H
"""


def fun(n, copy, paste, num_opt):
    """ return a number of operations """
    opt_2 = 0
    if paste > n:
        return 0
    if paste == n:
        return num_opt

    copy_1 = paste
    opt_1 = fun(n, copy_1, paste + copy_1, num_opt + 2)

    if paste != 1:
        opt_2 = fun(n, copy, paste + copy, num_opt + 1)

    if opt_1 != 0 and opt_2 != 0:
        return min(opt_1, opt_2)

    if opt_1 != 0 or opt_2 != 0:
        return max(opt_1, opt_2)
    return 0


def minOperations(n):
    """ return the fewest number of the operations """
    if n == 0 or n == 1:
        return 0

    return fun(n, 1, 1, 0)
