#!/usr/bin/python3
"""function of string format JSON to objt"""


import json


def from_json_string(my_str):
    """retur string json to object"""

    return json.loads(my_str)
