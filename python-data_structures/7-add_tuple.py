#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = tuple([tuple_a[i] + tuple_b[i] for i in range(len(tuple_a))])
    return (res)