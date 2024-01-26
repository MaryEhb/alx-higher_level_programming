#!/usr/bin/python3
"""6. POST an email #1"""

import sys
import requests

if __name__ == '__main__':
    res = requests.post(sys.argv[1], {'email': sys.argv[2]})
    print(res.text)
