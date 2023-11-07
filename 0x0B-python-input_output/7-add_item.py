#!/usr/bin/python3
"""7. Load, add, save"""
import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
write_file = __import__('1-write_file').write_file

try:
    jsonlist = load_from_json_file("add_item.json")
except FileNotFoundError:
    jsonlist = []

if len(sys.argv) > 1:
    newItems = sys.argv[1:]
    jsonlist.extend(newItems)

save_to_json_file(jsonlist, "add_item.json")
