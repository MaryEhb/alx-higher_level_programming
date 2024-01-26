#!/usr/bin/python3
"""3. Error code #0"""

from urllib import request, error
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
