#!/usr/bin/python3
""" Displays the value of the X-Request-Id """

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        holbi = response.headers.get('X-Request-Id')
        print(holbi)
