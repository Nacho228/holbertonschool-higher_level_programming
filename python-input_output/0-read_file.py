#!/usr/bin/python3
""" Task 0 """


def read_file(filename=""):
    """Read the contents of a file

    Args:
        filename (str, optional): _description_. Defaults to "".
    """
    with open(filename, encoding="utf-8") as f:
        read_text = f.read()
        print(f"{read_text}")
