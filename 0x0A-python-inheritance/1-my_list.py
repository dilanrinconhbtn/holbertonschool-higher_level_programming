#!/usr/bin/python3
"""
Class MyList
"""
class MyList(list):
    """
    Args:
        * l_sorted: Variable for stored the sorted list
        * self: variable that refers to the object itself
    """
    def print_sorted(self):
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
