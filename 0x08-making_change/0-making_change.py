#!/usr/bin/python3
""" change coin """


def makeChange(coins, total):
    """ make change """
    if total == 0:
        return 0
    db = [None] * (total + 1)
    db[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                count = 0
                count += 1
                result = i - coin
                if db[result] is not None:
                    count += db[result]
                    if db[i] is None or db[i] > count:
                        db[i] = count
    if db[total] is None:
        return -1
    return db[total]
