#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Validate if a given list of integers represents a valid UTF-8 encoding.

    Args:
    - data (list of integers): A list of integers representing a sequence of bytes.

    Returns:
    - bool: True if data is a valid UTF-8 encoding, else False.
    """
    byte_count = 0

    for i in data:
        if byte_count == 0:
            # Check for the start of a multi-byte character
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                byte_count = 1
            elif i >> 4 == 0b1110:
                byte_count = 2
            elif i >> 3 == 0b11110:
                byte_count = 3
            # Check for invalid leading byte
            elif i >> 7 == 0b1:
                return False
        else:
            # Check for continuation bytes
            if i >> 6 != 0b10:
                return False
            byte_count -= 1

    # This will Check if all expected continuation bytes were found
    return byte_count == 0
