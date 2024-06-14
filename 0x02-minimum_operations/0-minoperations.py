#!/usr/bin/python3
"""
calculate the number of the operations which will be taken
to reach the number of n which is the number of letter H
"""


def minOperations(n):
    """ we are get inside a loop and every iteration we will check
    if the paste which the number of letters H with the reqired number
    of H number which n.
    we will check if the remaing letters can be achived by past or
    copy all and paste and if the remaing is divisable by number of letters
    H which we have now we will copy all and paste othewise we will paste only
    with copy and paste all we will increase the num_opt by 2 because we copy
    and paste but if we are pasting only we will increase num_opt by 1"""
    if n == 0 or n == 1 or type(n) != int:
        return 0

    paste = 1
    copy = 1
    num_opt = 0

    while paste < n:

        if (n - paste) % paste == 0:
            copy = paste
            num_opt += 2
        else:
            num_opt += 1
        paste += copy

    return num_opt
