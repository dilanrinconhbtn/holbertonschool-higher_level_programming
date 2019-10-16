#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='utf-8') as file:
        if nb_lines <= 0:
            print(file.read(), end="")
        else:
            for l in range(nb_lines):
                print(file.readline(), end="")
