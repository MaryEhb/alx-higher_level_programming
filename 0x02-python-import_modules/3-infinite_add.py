#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    s = 0
    for n in args:
        s += int(n)

    print("{}".format(s))
