#!/usr/bin/python3
"""escribir una function que se pueda escribir"""


def write_file(filename="", text=""):
    """open filename and write text"""

    with open(filename, "w", encoding="utf-8") as w:
        return(w.write(text))
