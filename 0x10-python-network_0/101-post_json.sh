#!/bin/bash
#8. cURL a JSON file
curl -s "$1" -X POST -d @"$2" -H "Content-Type: application/json"
