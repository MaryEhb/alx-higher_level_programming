#!/usr/bin/python3
"""5. Response header value #1"""

import Requests
import sys

res = requests.get(sys.argv[1]).headers.get('X-Request-Id')
print(res)
