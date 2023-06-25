#!/usr/bin/python3
""" Geometry base """


class BaseGeometry():
    """Class BaseGeometry"""
    def area(self):
        """ Exception raise """
        raise Exception("area() is not implemented")
    pass

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        else:
            self.name = name


class Rectangle(BaseGeometry):
    """Rectangle class

    Args:
        inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """init"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
