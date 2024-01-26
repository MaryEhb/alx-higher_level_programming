#!/usr/bin/python3
"""8. Search API"""

import sys
import requests

if __name__ == '__main__':
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    res = requests.post('http://0.0.0.0:5000/search_user', {'q': q})
    try:
        json = res.json()

        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
