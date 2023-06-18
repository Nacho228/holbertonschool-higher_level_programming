#!/usr/bin/python3
"""more python classes"""


class Rectangle:
    """Simply defining a class"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Getter of the class instance width
            Return: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter of the class instance width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """" Getter of the class instance height
            Return: height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter of the class instance width """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Function that returns the area of a
        rectangle

        Returns:
            width * height
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        function that returns the perimeter
        of a rectangle

        Returns: rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2(self.__height + self.__width)
