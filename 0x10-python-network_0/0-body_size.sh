#!/usr/bin/env bash
# 0. cURL body size

if [ "$1" ]
then
	curl -Is "$1" | grep -Fi "Content-Length" | awk '{print $2}'
fi
