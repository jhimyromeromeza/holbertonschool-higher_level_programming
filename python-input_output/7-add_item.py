#!/usr/bin/python3
"""function that write a object and stores on file"""


from os import path
import json
import sys


def save_to_json_file(my_obj, filename):
    """write in a file"""

    with open(filename, "w") as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """return of filename to object"""

    with open(filename, "r") as f:
        return json.load(f)


if __name__ == "__main__":
    filename = "add_item.json"
    if path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, filename)
