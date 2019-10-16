#!/usr/bin/python3
def number_of_lines(filename=""):
    line_numbers = 0
    with open(filename, encoding='utf-8') as f:
        for lines in f:
            line_numbers += 1
    return (line_numbers)
