#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = my_list.copy()
    if idx >= 0 and idx < (len(new)):
        new[idx] = element
    else:
        return my_list
    return new
