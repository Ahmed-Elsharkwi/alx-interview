#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""
import signal
import re
import sys


def happen(size, states_code):
    """ happen """
    print(f"File size: {size}")
    for code in states_code:
        if states_code[code] != 0:
            print(f"{code}: {states_code[code]}")


def main():
    """ main function """
    size = 0
    states_code = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    counter = 1
    try:
        for line in sys.stdin:
            elements = line.split(" ")
            res = re.search(
                r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
                r'\s\-\s\[\d{4}\-\d{2}\-\d{2}\s\d{2}\:'
                r'\d{2}\:\d{2}\.\d+\]\s\"GET\s/projects/260\sHTTP/1.1\"'
                r'\s\d{1,3}\s\d{1,4}$', line)
            if res is not None:
                size += int(elements[8])
                if int(elements[7]) in states_code:
                    states_code[int(elements[7])] += 1

                if counter == 10:
                    happen(size, states_code)
                    counter = 0
                counter += 1
    except KeyboardInterrupt:
        happen(size, states_code)


if __name__ == '__main__':
    main()
