#!/usr/bin/python3
""" Another class, rectangle this time """
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base
    class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes attributes

        Args:
            width (int): Rectangle width
            height (int): Rectangle height
            x (int, optional): Width number. Defaults to 0.
            y (int, optional): Height number. Defaults to 0.
            id inherited from super().
        """
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)
        self.__x = x
        self.x_or_y("x", x)
        self.__y = y
        self.x_or_y("y", y)
        super().__init__(id)
        


"Getters and setter"


@property
def width(self):
    """ width getter """
    return self.__width


@width.setter
def width(self, value):
    """width setter"""
    self.__width = value


@property
def height(self):
    """height getter"""
    return self.__height


@height.setter
def height(self, value):
    """heigth setter"""
    self.__height = value


@property
def x(self):
    """x getter"""
    return self.__x


@x.setter
def x(self, value):
    """x setter"""
    self.__x = value


@property
def y(self):
    """y getter"""
    return self.__y


@y.setter
def y(self, value):
    """y setter"""
    self.__y = value
