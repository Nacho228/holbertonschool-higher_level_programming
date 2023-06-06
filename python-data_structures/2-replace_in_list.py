#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx not in range(len(my_list)) or idx < 0:
        return my_list
    else:
        if idx < element:
            my_list[idx] = element
            return my_list
        else:
            return my_list
