#!/usr/bin/python3
"""test test"""


class Square:
    """test test"""

    __size = 0
    __position = 0

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
        """pos set"""

        testL = len(value) != 2
        testT = not isinstance(value[0], int)
        testT_ = not isinstance(value[1], int)
        testV1 = value[0] < 0
        testV2 = value[1] < 0
        test = testL or testT or testT_ or testV1 or testV2
        if test:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __init__(self, size=0, position=(0, 0)):
        """why this"""

        testL = len(position) != 2
        testT = not isinstance(position[0], int)
        testT_ = not isinstance(position[1], int)
        testV1 = position[0] < 0
        testV2 = position[1] < 0
        test = testL or testT or testT_ or testV1 or testV2
        if test:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
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
