#!/usr/bin/python3
""" Geometry base """


class BaseGeometry:

    def area(self):
        """ Exception raise """
        raise Exception("area() is not implemented")
    pass

    def integer_validator(self, name, value):
        self.name = name
        if type(value) is not int:
            TypeError("<name> must be an integer")
        elif value <= 0:
            ValueError("<name> must be greater than 0") 

