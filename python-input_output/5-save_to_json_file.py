#!/usr/bin/python3
"""function that write a object and stores on file"""


import json


def save_to_json_file(my_obj, filename):
    """write in a file"""

    with open(filename, "w") as mw:
        json.dump(my_obj, mw)
