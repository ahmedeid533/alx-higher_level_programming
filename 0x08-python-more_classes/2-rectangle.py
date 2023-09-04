#!/usr/bin/python3
"""react angle class"""


class Rectangle:
    """rectangel class"""

    __height = 0
    __width = 0

    @property
    def width(self):
        """get W"""

        return self.__width

    @width.setter
    def width(self, value):
        """set W"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get H"""

        return self.__height

    @height.setter
    def height(self, value):
        """set H"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    def area(self):
        """calculate area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """calculate perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width * self.__height)
