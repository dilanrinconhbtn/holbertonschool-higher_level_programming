#!/usr/bin/python3
for first_digit in range(0, 10):
    for second_digit in range(0,10):
        print("{}{}".format(first_digit, second_digit), end='')
        if first_digit != 9 or second_digit != 9:
            print(", ", end='')
