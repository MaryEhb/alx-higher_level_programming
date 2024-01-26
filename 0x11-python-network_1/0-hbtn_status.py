#!/usr/bin/python3
# 0. What's my status? 0

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
    body = res.read()
    print("Body response:\n\
    \t- type: {}\n\
    \t- content: {}\n\
    \t- utf8 content: {}".format(type(body), body, body.decode('utf-8')))
