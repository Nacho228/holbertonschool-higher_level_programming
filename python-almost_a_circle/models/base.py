#!/usr/bin/python3
""" task 1 python almost a circle"""


class Base:
    """Base class

    Raises:
        TypeError: checks for typeerror
        ValueError: checks for valueerror
        TypeError: checks for typerror
        ValueError: checks for valuerror
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization of id"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.name = value

    def x_or_y(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")
        self.name = value
