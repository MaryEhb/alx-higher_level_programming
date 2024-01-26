#!/usr/bin/python3
"""5. Response header value #1"""

import requests
import sys

if __name__ == '__main__':
    res = requests.get(sys.argv[1]).headers.get('X-Request-Id')
    print(res)
