#!/usr/bin/python3
"""1. Base class"""


class Base:
    """Base class with private attr nb_objects"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
