#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    maximum = 0
    for i in range(len(my_list)):
        if maximum < my_list[i]:
            maximum = my_list[i]
    return maximum
