#!/usr/bin/python3
"""class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Rectangle implemntation"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        """"print rect info"""
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
