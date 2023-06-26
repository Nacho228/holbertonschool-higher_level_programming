#!/usr/bin/python3
""" task 1 python almost a circle"""


class Base:
    """Base class"""

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
        else:
            self.name = name

    
    def x_or_y(self, name, value):
        if value < 0:
            raise ValueError(f"{name} must be >= 0")
        else:
            self.value = value
            self.name = name
