#!/bin/bash
#7. Only status code
curl -si "$1" | grep -Fi "HTTP" | cut -d " " -f2
