#!/usr/bin/python3
class Square:
    val = {}
    def __init__(self):
        self.__dict__ = self.val
