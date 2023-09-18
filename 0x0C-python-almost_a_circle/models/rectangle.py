#!/usr/bin/python3
"""class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """rect of class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init the rect"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get W"""

        return self.__width

    @width.setter
    def width(self, value):
        """set W"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x"""

        return self.__x

    @x.setter
    def x(self, value):
        """set x"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y"""

        return self.__y

    @y.setter
    def y(self, value):
        """set y"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate area"""
        return (self.__width * self.__height)

    def display(self):
        """"print rect of # with x y offset"""

        temp = ""
        if self.width == 0 or self.height == 0:
            temp = ""
        else:
            for newL in range(self.y):
                temp += "\n"

            for i in range(self.height):
                for newS in range(self.x):
                    temp += " "
                for j in range(self.width):
                    temp += "#"
                temp += "\n"
        print(temp, end="")

    def __str__(self):
        """"print rect info"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.x, self.y,
                                                        self.width,
                                                        self.height))

    def update(self, *args, **kwargs):
        """update exist rect"""
        values = [self.id, self.width, self.height, self.x, self.y]
        keys = ["id", "width", "height", "x", "y"]
        i = 0
        if args and len(args) != 0:
            for arg in args:
                if arg:
                    values[i] = arg
                    i += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                for k in keys:
                    if k == key:
                        values[i] = value
                    i += 1
                i = 0
        self.id = values[0]
        self.width = values[1]
        self.height = values[2]
        self.x = values[3]
        self.y = values[4]

    def to_dictionary(self):
        """rect to dict """
        diction = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return diction
