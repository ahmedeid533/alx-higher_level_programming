#!/usr/bin/python3
"""class Rectangle"""


class Rectangle(BaseGeometry):
    """class Rectangle implemntation"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(width)
        BaseGeometry.integer_validator(height)
        self.__width = width
        self.__height = height

