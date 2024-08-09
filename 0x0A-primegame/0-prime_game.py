#!/usr/bin/python3
"""
solve the prime game
"""


def check_the_prime_number(number):
    """
    it will check if the number is prime or not
    """
    if number == 1:
        return 0
    counter = 2
    number_factors = 0

    while (counter <= int(number / 2)):
        if number_factors > 1:
            return 0
        if number % counter == 0:
            number_factors += 1
        counter += 1
    return 1


def del_target_number(number, num_list):
    """ delete the target numbers """
    length = len(num_list)
    i = 0
    while i < length:
        if num_list[i] % number == 0:
            del num_list[i]
            length -= 1
        else:
            i += 1
    return length


def isWinner(x, nums):
    """ decide who is winner """

    maria_score_rounds = 0
    ben_score_rounds = 0

    for i in range(0, x):
        num_list = []
        maria_score = 0
        maria_status = 0
        ben_score = 0
        ben_status = 1
        length = 0
        index = 0
        for num in range(1, nums[i] + 1):
            num_list.append(num)
            length += 1

        while index <= length:
            if (index != length) and (
                    check_the_prime_number(num_list[index]) == 1):

                length = del_target_number(num_list[index], num_list)

                if maria_status == 0:
                    maria_score += 1
                    maria_status = 1
                    ben_status = 0

                elif ben_status == 0:
                    ben_score += 1
                    ben_status = 1
                    maria_status = 0
            else:
                if index == length:
                    if maria_status == 1:
                        maria_score += 1
                    if ben_status == 1:
                        ben_score += 1
                index += 1

        if maria_score > ben_score:
            maria_score_rounds += 1
        elif ben_score > maria_score:
            ben_score_rounds += 1
    if maria_score_rounds > ben_score_rounds:
        return "Maria"
    elif ben_score_rounds > maria_score_rounds:
        return "Ben"
    else:
        return None
