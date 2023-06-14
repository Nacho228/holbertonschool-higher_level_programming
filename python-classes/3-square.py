#!/usr/bin/python3
"""tarea toomfoolery"""


class Square:
    """
        A Square class that handles certain errors of certain class
        (or not) attributes (or not).
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ A simple function that returns the area of 
        the class of self.

        Returns: Square area.
        """
        return (self.__size * self.__size)
