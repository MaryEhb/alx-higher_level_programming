#!/usr/bin/python3
"""9. Student to JSON"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__.copy()

    def to_json(self, attrs=None):
        dic = self.__dict__.copy()

        if isinstance(attrs, list):
            newdic = {}
            for item in attrs:
                if item in dic:
                    newdic[item] = dic[item]
            return newdic

        else:
            return dic

    def reload_from_json(self, json):
        for i in json:
            self.__dict__[i] = json[i]
