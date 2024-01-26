#!/usr/bin/python3
"""7. Error code #1"""

import requests
import sys

if __name__ == '__main__':
    res = requests.get(sys.argv[1])
    if res.status_code < 400:
        print(res.text)
    else:
        print("Error code: ".format(res.status_code))
