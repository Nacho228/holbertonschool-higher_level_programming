#!/usr/bin/python3
"""TASK 1"""


def write_file(filename="", text=""):
    with open(filename, "w+", encoding="utf-8") as f:
        written = f.write(text)
        return written
