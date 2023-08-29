#!/usr/bin/python3
"""test test"""


class Square:
    """test test"""

    def __init__(self, size=0):
        """why this"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculate area"""
        return (self.__size ** 2)
