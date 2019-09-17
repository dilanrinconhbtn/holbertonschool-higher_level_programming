#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sizea = len(tuple_a)
    sizeb = len(tuple_b)
    for i in range(sizea):
        if sizea < 2:
            tuple_a += (0,)
        elif sizeb < 2:
            tuple_b += (0,)
    c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return c
