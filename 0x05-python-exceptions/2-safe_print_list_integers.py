#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    length = 0
    for e in range(x):
        try:
            print("{:d}".format(my_list[e]), end="")
            length += 1
        except ValueError:
            continue
        except TypeError:
            continue
    print("")
    return length
