#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < element or idx < 0:
        my_list[idx] = element
        return my_list
    else:
        return my_list
