#!/usr/bin/python3
def add_integer(a, b=98):
    """Addition function"""
    if not isinstance(a, int):
        if type(a) is float:
            int(a)
        else:
            raise TypeError("a must be an integer")
    if not isinstance(b, int):
        if type(b) is float:
            int(b)
    else:
        return (a + b)
    