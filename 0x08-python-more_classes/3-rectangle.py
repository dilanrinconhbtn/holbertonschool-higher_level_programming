#!/usr/bin/python3
class Rectangle:
    """
    Class Rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("wigth must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("wigth must be >= 0")
        self.__height = value

    def area(self):
        """
        Area of a rectangle
        """
        return (self.__width) * (self.__height)

    def perimeter(self):
        """
        Perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            cadena = ""
            for row in range(self.__height):
                for col in range(self.__width):
                    cadena = cadena+"#"
                if row < self.__height - 1:
                    cadena = cadena+"\n"
            return cadena
