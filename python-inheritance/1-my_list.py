#!/usr/bin/python3
"""class MyList inheritance list"""


class MyList(list):
    """metodo instancia que ordena"""

    def print_sorted(self):
        print(sorted(self))
