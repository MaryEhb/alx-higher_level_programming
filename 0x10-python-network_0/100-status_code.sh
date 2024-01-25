#!/bin/bash
#7. Only status code
curl -si "$1" -o /dev/null -w "%{http_code}"
