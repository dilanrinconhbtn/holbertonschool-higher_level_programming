#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last_digit = number % 10
if number < 0:
    last_digit = -number % 10
if last_digit > 5:
    the_string = "and is greater than 5"
elif last_digit == 0:
    the_string = "and is 0"
elif last_digit < 6:
    the_string = "and is less than 6 and not 0"
if number < 0:
    the_string = "and is less than 6 and not 0"
    print("Last digit of {} is -{} {}".format(number, last_digit,
                                              the_string))
else:
    print("Last digit of {} is {} {}".format(number, last_digit,
                                             the_string))
