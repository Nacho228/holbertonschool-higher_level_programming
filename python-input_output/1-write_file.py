#!/usr/bin/python3
"""TASK 1"""


def write_file(filename="", text=""):
    """_summary_

    Args:
        filename: name of the file to be written on. Defaults to "".
        text: text to be written with. Defaults to "".

    Returns:
        Number of characters written
    """
    with open(filename, "w+", encoding="utf-8") as f:
        written = f.write(text)
        return written
