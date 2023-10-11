#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    new_dict = dict()
    for i in a_dictionary.keys():
        new_dict[i] = a_dictionary.get(i)

    new_dict[key] = value
    return new_dict
