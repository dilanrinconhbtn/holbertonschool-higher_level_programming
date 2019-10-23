#!/usr/bin/python3
"""Class Rectangle that is child of Base """
from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialitation
        args:
            id: integer value
            width: width
            height: height
            x: x
            y: y"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area = return area of rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """print a rectangle with #"""
        for l_y in range(self.__y):
            print()
        for row in range(self.__height):
            for l_x in range(self.__x):
                print(" ", end="")
            for col in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """return string"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """update the arguments"""
        if args is None and len(args) is not 0:
            argumentos = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, argumentos[i], args[i])
        else:
            for arg, value in kwargs.items():
                setattr(self, arg, value)

    def to_dictionary(self):
        """Class rectangle representate in a dictionary form"""
        argumentos = ['id', 'width', 'height', 'x', 'y']
        for i in range(len(argumentos)):
            return {'id': getattr(self, argumentos[0]),
                    'width': getattr(self, argumentos[1]),
                    'height': getattr(self, argumentos[2]),
                    'x': getattr(self, argumentos[3]),
                    'y': getattr(self, argumentos[4])}
