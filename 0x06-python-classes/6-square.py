#!/usr/bin/python3
class Square:
    """Class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """__init__ method.
        Args:
        size (int): size of the square
        position: tuple of two elements
        """
        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """area method"""
        return self.__size * self.__size

    @property
    def position(self):
        """ setter of position """
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and value >= 0:
            if len(value) is 2:
                for v in value:
                    if isinstance(v, int):
                        self.__position = value
                    else:
                        raise TypeError("position must be a tuple of 2 positive integers")
            else:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """ setter and getter modifying a value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) and value >= 0:
            self.__size = value
        elif not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """print square #"""
        if isinstance(self.size, int) and self.size >= 0:
            if self.size is 0:
                print()
            else:
                for filas_vacias in range(self.position[1]):
                    print()
                for filas in range(self.size):
                    for columnas in range(self.size):
                        for espacios in range(self.__position):
                            print(" ", end='')
                        print("#", end='')
                    print()
        elif not isinstance(self.size, int):
            raise TypeError("size must be an integer")
        elif self.size < 0:
            raise ValueError("size must be >= 0")
