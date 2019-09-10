#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        num_letter = ord(str[i])
        if num_letter in range(97, 123):
            num_letter = num_letter - 32
            num_letter = chr(num_letter)
        else:
            num_letter = chr(num_letter)
        print("{}".format(num_letter), end='')
    print()
