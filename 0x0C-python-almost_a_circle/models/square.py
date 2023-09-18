#!/usr/bin/python3
"""class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """imp of the class"""
    def __init__(self, size, x=0, y=0, id=None):
        """init of init of square rect"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """"print square info"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                                                  self.x, self.y,
                                                  self.width))

    @property
    def size(self):
        """get size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size from width height setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update exist square"""
        values = [self.id, self.size, self.x, self.y]
        keys = ["id", "size", "x", "y"]
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
        self.size = values[1]
        self.x = values[2]
        self.y = values[3]

    def to_dictionary(self):
        """square to dict """
        diction = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return diction
