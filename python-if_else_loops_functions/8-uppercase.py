#!/usr/bin/python3
def uppercase(str):

    for i in range(0, len(str)):
        x = ord(str[i])
        if x >= 96 and x <= 122:
            x = x - 32
        y = chr(x)
        txt = "{}"
        print(txt.format(y), end="")
    print()
