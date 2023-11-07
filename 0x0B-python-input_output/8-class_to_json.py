#!/usr/bin/python3
"""8. Class to JSON"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    serialization of an object"""

    dic = {}
    if hasattr(obj, "__dict__"):
        dic = obj.__dict__.copy()
    return dic
