#!/usr/bin/python3
"""function to add two integers"""


def add_integer(a, b=98):
    """
    add two integers

    Args:
        a: num
        b: num

    Return: sum
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
