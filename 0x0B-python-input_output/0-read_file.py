#!/usr/bin/python3
"""0. Read file"""

def read_file(filename=""):
    """read file and print content"""
    with open(filename, 'r') as file:

        for line in file:
            print(line)
