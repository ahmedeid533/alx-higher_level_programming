#!/usr/bin/python3
"""class"""


class BaseGeometry():
    """class"""
    def area(self):
        """raise error"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """vaidation"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))
