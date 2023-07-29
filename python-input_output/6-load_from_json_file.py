#!/usr/bin/python3
"""function that creates an object fron filejson"""


import json


def load_from_json_file(filename):
    """return of filename to object"""

    with open(filename, "r") as f:
        return json.load(f)
