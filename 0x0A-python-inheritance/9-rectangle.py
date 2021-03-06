#!/usr/bin/python3
""" class BaseGeometry"""


class BaseGeometry():
    def area(self):
        """ area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate value is integer grather than 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

""" class Rectangle"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ mod print"""
        return("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """ area = sidth * height"""
        return self.__width * self.__height
