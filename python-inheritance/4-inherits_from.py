#!/usr/bin/python3
""" task 2 """


def inherits_from(obj, a_class):
    """ is same class """
    if not type(obj) is a_class:
        if isinstance(obj, a_class):
            return True
    else:
        return False
