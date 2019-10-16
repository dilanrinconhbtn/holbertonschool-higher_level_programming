#!/usr/bin/python3
import json


def load_from_json_file(filename):
    with open(filename, encoding='utf-8') as f:
        v_js = f.read()
    return(json.loads(v_js))
