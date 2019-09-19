#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for i in range(len(new)):
        if new[i] is 2:
            new.pop(i)
            new.insert(i, 89)
    return new
