#!/usr/bin/python3
"""0. What's my status? 0"""

import urllib.request

if __name__ == '__main__':

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        body = res.read()
        str = "Body response:\n\t- type: {}".format(type(body))
        str += "\n\t- content: {}".format(body)
        str += "\n\t- utf8 content: {}".format(body.decode('utf-8'))
        print(str)
