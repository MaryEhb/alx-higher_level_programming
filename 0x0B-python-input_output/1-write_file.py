#!/usr/bin/python3


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="UTF8") as file:
        file.write(text)
    return len(text)

