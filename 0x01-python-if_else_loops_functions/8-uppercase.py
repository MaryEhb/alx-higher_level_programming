#!/usr/bin/python3
def uppercase(str):
    newstr = ""
    for c in str:
        if ord(c) >= 97 and ord(c) < 123:
            c = chr(ord(c) - 32)
        newstr += c
    print("{}".format(newstr))
