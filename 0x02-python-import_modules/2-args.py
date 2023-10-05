#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]

    print("{} arguments.".format(len(args)))

    if len(args) > 0:
        for i in range(1, len(args) + 1):
            print("{}: {}".format(i, args[i - 1]))
