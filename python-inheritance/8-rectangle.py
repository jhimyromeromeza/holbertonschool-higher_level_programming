#!/usr/bin/python3
"""class Rectangle"""


from base_geometry import BaseGeometry
class Rectangle(BaseGeometry):
    """metodo de instancia __init__"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
