#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for iterable, i in enumerate(my_list[::-1]):
        print("{:d}".format(i))
