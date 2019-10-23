#!/usr/bin/python3
""" square Class child of Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """ initialitation """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return string"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                                                  self.x, self.y, self.width))

    @property
    def size(self):
        """size"""
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """update values"""
        if args is not None and len(args) != 0:
            argumentos = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, argumentos[i], args[i])
        else:
            for arg, value in kwargs.items():
                setattr(self, arg, value)

    def to_dictionary(self):
        """class square representate in dictionary form"""
        argumentos = ['id', 'size', 'x', 'y']
        for i in range(len(argumentos)):
            return {'id': getattr(self, argumentos[0]),
                    'size': getattr(self, argumentos[1]),
                    'x': getattr(self, argumentos[2]),
                    'y': getattr(self, argumentos[3])}
