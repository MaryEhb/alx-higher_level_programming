#!/bin/bash
# 1. cURL to the end
curl -s "$1" | grep -v "HTTP/"
