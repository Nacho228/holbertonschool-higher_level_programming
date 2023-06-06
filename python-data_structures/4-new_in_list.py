#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = my_list.copy()
    if idx not in range(len(my_list) - 1) or idx < 0:
        return copy_list
    else:
        copy_list[idx] = element
        return copy_list
