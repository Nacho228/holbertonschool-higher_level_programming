#!/usr/bin/python3
"""tarea toomfoolery"""


class Square:
    """
        A Square class that handles certain errors of certain class
        (or not) attributes (or not).
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            self.__size = size
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ A simple function that returns the area of
        the class of self.

        Returns: Square area.
        """
        return (self.__size * self.__size)

    def my_print(self):
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end="")
            print()
