#!/bin/bash
#3. cURL only methods
curl -sI "$1" | grep -Fi "Allow" | cut -d " " -f2-
