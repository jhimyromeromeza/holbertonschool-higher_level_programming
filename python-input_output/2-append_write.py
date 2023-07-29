#!/usr/bin/python3i
"""function append to file"""


def append_write(filename="", text=""):
    """mode append text to an file"""

    with open(filename, "a", encoding="utf-8") as a:
        return a.write(text)
