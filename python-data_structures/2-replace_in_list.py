#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx + 1 not in range(len(my_list)):
        return my_list
    else:
        if idx < element or idx < 0:
            my_list[idx] = element
            return my_list
        else:
            return my_list
