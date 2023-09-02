#!/usr/bin/python3
"""test example"""


def add_integer(a, b=98):
    """add intgers"""
    if (not isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    elif (not isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    a_ = int(a)
    b_ = int(b)
    return a_ + b_
