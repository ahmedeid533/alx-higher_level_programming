#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key == "":
        return a_dictionary
    del a_dictionary[key]
    return a_dictionary
