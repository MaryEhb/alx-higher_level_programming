#!/bin/bash
# 0. cURL body size
curl -Is "$1" | grep -Fi "Content-Length" | awk '{print $2}'
