#!/usr/bin/python3
"""function than comparation"""


def inherits_from(obj, a_class):
    """return True or False"""

    return issubclass(type(obj), a_class) or type(obj) =! a_class
