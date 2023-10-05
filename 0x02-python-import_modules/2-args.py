#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]

    if len(args) > 0:
        print("{} arguments:".format(len(args)))
        for i in range(1, len(args) + 1):
            print("{}: {}".format(i, args[i - 1]))
    else:
        print("0 arguments.")
