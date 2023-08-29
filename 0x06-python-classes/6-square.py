#!/usr/bin/python3
"""test test"""


class Square:
    """test test"""

    __size = 0
    __position = (0, 0)

    @property
    def size(self):
        """why this"""

        return self.__size

    @size.setter
    def size(self, value):
        """why this"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """pos"""

        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2 or not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
        
    def __init__(self, size=0, position=(0, 0)):
        """why this"""

        if len(position) != 2 or not isinstance(position[0], int) or not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        """calculate area"""
        return (self.__size ** 2)

    def my_print(self):
        """print square of #"""

        if self.__size == 0:
            print("")
        else:
            for newL in range(self.__position[1]):
                print("")

            for i in range(self.__size):
                for newS in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
