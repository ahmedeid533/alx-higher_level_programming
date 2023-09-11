#!/usr/bin/python3
"""is subbclass"""


def is_kind_of_class(obj, a_class):
    """is subbclass"""
    if type(obj) == a_class:
        return True
    return issubclass(type(obj), a_class)
