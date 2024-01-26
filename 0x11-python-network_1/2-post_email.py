#!/usr/bin/python3
# 2. POST an email

import sys
from urllib import request, parse

if __name__ == '__main__':

    headers = parse.urlencode({'email': sys.argv[2]}).encode('utf-8')

    with request.urlopen(sys.argv[1], headers) as res:
        body = res.read().decode('utf-8')
        print(body)
