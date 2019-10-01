#!/usr/bin/python3
class Square:
    """Class Square"""
    def __init__(self, size=0):
        """__init__ method.
        Args:
        param1 (str): Description of `param1`.
        param2 (:obj:`int`, optional): Description of `param2`. Multiple
        lines are supported.
        param3 (:obj:`list` of :obj:`str`): Description of `param3`.
        size (int): size of the square
        """
        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
