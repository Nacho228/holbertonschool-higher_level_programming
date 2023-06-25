#!/usr/bin/python3
""" task 2 """


def inherits_from(obj, a_class):
    """ is same class """
    return issubclass(type(obj), a_class) and type(obj) != a_class
