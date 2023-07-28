#!/usr/bin/python3
"""class Rectangle"""



class Rectangle(BaseGeometry):
    """metodo de instancia __init__"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
