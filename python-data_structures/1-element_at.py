#!/usr/bin/python3
def element_at(my_list, idx):
    if idx in my_list:
        return my_list[idx]
    elif idx in range(len(my_list)):
        return my_list[idx]
    else:
        return
