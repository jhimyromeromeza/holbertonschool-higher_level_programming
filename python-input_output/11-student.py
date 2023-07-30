#!/usr/bin/python3
"""class Student"""


class Student:
    """metodo de instnacia init"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return list of atributes and value"""

        if attrs is None:
            return self.__dict__
        else:
            deposito = {}
            for i in attrs:
                if hasattr(self, i):
                    deposito[i] = getattr(self, i)

            return deposito
    
    def reload_from_json(self, json):
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
