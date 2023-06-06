#!/usr/bin/python3
def element_at(my_list, idx):
    if idx in my_list or idx not in range(my_list):
        return my_list[idx]
