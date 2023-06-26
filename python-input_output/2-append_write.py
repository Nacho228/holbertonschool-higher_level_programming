#!/usr/bin/python3
"""Task 2"""


def append_write(filename="", text=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".
    """
    with open(filename, "a+", encoding="utf-8") as f:
        appended = f.write(text)
        return appended
