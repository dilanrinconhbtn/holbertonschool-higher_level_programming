#!/usr/bin/python3
""" class patern"""


class BaseGeometry():
    def area(self):
        """ area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate value if is integer grater than 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

""" Class Rectangle"""


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """mod the print"""
        return("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """area = width * height"""
        return self.__width * self.__height

""" Square child of BaseGeometry"""


class Square(BaseGeometry):
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """ mod print """
        return("[Rectangle] {:d}/{:d}".format(self.__size, self.__size))

    def area(self):
        """ area = size * size"""
        return self.__size * self.__size
