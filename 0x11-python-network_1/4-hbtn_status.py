#!/usr/bin/python3
"""4. What's my status? #1"""

import requests

if __name__ == '__main__':
    res = requests.get('https://alx-intranet.hbtn.io/status')
    str = "Body response:\n\t- type: {}".format(type(res.text))
    str += "\n\t- content: {}".format(res.text)
    print(str)
