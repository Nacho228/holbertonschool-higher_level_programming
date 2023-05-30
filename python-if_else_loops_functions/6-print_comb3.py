#!/usr/bin/python3
for tens in range(9):
    for ones in range(tens + 1, 10):
        print("{}{}".format(tens, ones), end=", " if tens < 8 else " ")
print()
