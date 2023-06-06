#!/usr/bin/python3
def element_at(my_list, idx):
    if idx in my_list or idx < len(my_list) - 1:
        return my_list[idx]
