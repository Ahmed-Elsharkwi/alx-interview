#!/usr/bin/python3
""" validation module """


def validUTF8(data):
    """ utf-8 validation """
    binary_list = []
    res = False
    counter = 0

    for element in data:
        binary_element = bin(element)[2:]
        length = len(binary_element)

        if length < 8:
            binary_element = ('0' * (8 - length)) + str(binary_element)

        binary_list.append(binary_element)

    while counter < len(binary_list):

        if binary_list[counter][0] == '0':
            counter += 1
            res = True
            continue

        elif binary_list[counter][0:3] == '110':
            limit = 2

        elif binary_list[counter][0:4] == '1110':
            limit = 3

        elif binary_list[counter][0:5] == '11110':
            limit = 4

        i = 1
        while i < limit:
            if binary_list[counter + i][0:1] == '10':
                res = True
            else:
                return False
            counter += 1
        counter = i

    return res
