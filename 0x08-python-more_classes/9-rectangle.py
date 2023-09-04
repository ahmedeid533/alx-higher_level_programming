#!/usr/bin/python3
"""react angle class"""


class Rectangle:
    """rectangel class"""

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

    def area(self):
        """calculate area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """calculate perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    @classmethod
    def square(cls, size=0):
        return (cls(size, size))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """"print rect of #"""

        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the opject inti"""
        return (f"Rectangle({str(self.__width)}, {str(self.__height)})")

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
