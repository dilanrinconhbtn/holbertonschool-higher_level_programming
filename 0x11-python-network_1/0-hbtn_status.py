#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        holbi = response.read()
        print("Body response:")
        print("\t- type: " + str(type(holbi)))
        print("\t- content: " + str(holbi))
        print("\t- utf8 content: " + holbi.decode('utf-8'))