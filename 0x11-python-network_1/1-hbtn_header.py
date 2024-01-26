#!/usr/bin/python3
# 1. Response header value

import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as res:
    result = res.getheader('X-Request-Id')
    print(result)
