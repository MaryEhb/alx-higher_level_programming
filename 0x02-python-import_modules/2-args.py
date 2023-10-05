#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]

    if len(args) > 0:
        if len(args) == 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(len(args)))
        for i in range(len(args)):
            print("{}: {}".format(i + 1, args[i]))
    else:
        print("0 arguments.")
