#!/usr/bin/python3
"""New class"""
from models.rectangle import Rectangle
import json


class Square(Rectangle):
    """Class Square that inherits from
    rectangle.

    Args:
        Square: with all attributes.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """updates and assigns attributes to a
        variable number of arguments
        """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for arg, attr in zip(args, attrs):
                setattr(self, attr, arg)
        elif kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ Rectangle instance to dictionary representation """
        return dict(id=self.id, size=self.size, x=self.x, y=self.y)
