#!/usr/bin/python3
"""function filename open"""


def read_file(filename=""):
    """function using with for print"""

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
