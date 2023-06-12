#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{}".format(value))
            return True
    except ValueError:
        pass
    else:
        return False
