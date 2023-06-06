#!/usr/bin/python3
def element_at(my_list, idx):
    if idx + 1 in my_list:
        return my_list[idx]
    elif idx in range(len(my_list) - 1):
        return my_list[idx]
    else:
        return None
