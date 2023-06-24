#!/usr/bin/python3
""" task 2 """


def is_kind_of_class(obj, a_class):
    """ is same class """
    if isinstance(obj, a_class):
        return True
    else:
        return False
