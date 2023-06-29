#!/usr/bin/python3
"""New class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from
    rectangle.

    Args:
        Square: with all attributes.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return super().__str__()
