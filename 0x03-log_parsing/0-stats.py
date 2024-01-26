#!/usr/bin/python3

import sys


def greatest(dict_s, total_file_size):
    """
    method to print
    Args:
        dict_s: dict of status codes
        total_file_size:this is total file size
    returns:
        Nothing
    """

    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_s.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_file_size = 0
code = 0
counter = 0
dict_s = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]
        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(parsed_line[0])
                code = parsed_line[1]
                if (code in dict_s.keys()):
                    dict_s[code] += 1

            if (counter == 10):
                greatest(dict_s, total_file_size)
                counter = 0

finally:
    greatest(dict_s, total_file_size)