#!/usr/bin/python3
def uniq_add(my_list=[]):
    ans = 0
    new = set(my_list)
    for i in new:
        ans = ans + i
    return ans
