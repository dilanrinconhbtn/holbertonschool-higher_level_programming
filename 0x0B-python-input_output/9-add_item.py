#!/usr/bin/python3
import os
import sys
save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file


lis = []

if os.path.exists('add_item.json'):
    lis = list(load("add_item.json"))

for i in range(1, len(sys.argv)):
    lis.append(sys.argv[i])

save(lis, "add_item.json")
