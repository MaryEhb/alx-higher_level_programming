#!/usr/bin/python3
"""9. My GitHub!"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    credintials = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get("https://api.github.com/user", credintials)
    print(res.json().get("id"))
