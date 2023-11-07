#!/usr/bin/python3
"""5. Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""

    my_obj_str = json.dumps(my_obj)
    with open(filename, 'w') as f:
        f.write(my_obj_str)
