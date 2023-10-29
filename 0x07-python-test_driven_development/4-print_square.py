#!/usr/bin/python3
"""3. Print square"""


def print_square(size):
    """
    function that prints a square with the character #

    Args:
        size: is the size length of the square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    print(("#" * size + "\n") * size, end="")
