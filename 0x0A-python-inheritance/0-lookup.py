#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """list of an object's attributes."""
    lst = dir(obj)
    return lst
