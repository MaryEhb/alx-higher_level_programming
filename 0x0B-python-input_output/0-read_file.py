#!/usr/bin/python3
"""0. Read file"""


def read_file(filename=""):
    """read file and print content"""
    with open(filename, 'r', encoding="UTF-8") as file:
        print(file.read(), end="")
