#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) >= 96 and ord(str[i]) <= 123:
            print(chr(ord(str[i]) - 32), end="")
        else:
            print(str[i], end="")
    print()
