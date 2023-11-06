#!/usr/bin/python3
"""1. My list"""


class MyList(list):
    """ a class MyList that inherits from list """

    def print_sorted(self):
        """Print list sorted ascendingly"""
        print(sorted(self))
