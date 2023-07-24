#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return 0
    suma = sum(x * y for x, y in my_list)
    resultado = sum(y for x, y in my_list)
    return suma / resultado
