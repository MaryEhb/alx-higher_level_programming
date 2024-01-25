#!/bin/bash
#3. cURL only methods
curl -s $1 -X OPTIONS | grep -Fi "Allow" | cut -d " " -f2-
