#!/usr/bin/python3
""" Base Geometry"""


class BaseGeometry():
    def area(self):
        """ area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate value if is integer and grather than 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
