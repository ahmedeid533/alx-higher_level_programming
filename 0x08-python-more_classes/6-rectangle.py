#!/usr/bin/python3
"""react angle class"""


class Rectangle:
    """rectangel class"""

    __height = 0
    __width = 0
    number_of_instances = 0

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
        self.number_of_instances += 1

    def area(self):
        """calculate area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """calculate perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """"print rect of #"""

        temp = ""
        if self.__width == 0 or self.__height == 0:
            temp = ""
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    temp += "#"
                if i < self.__height - 1:
                    temp += "\n"
        return str(temp)

    def __repr__(self):
        """Return the opject inti"""
        return (f"Rectangle({str(self.__width)}, {str(self.__height)})")

    def __del__(self):
        self.number_of_instances -= 1
        print("Bye rectangle...")
