#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    sin_modificar = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return my_list
    sin_modificar[idx] = element
    return sin_modificar
