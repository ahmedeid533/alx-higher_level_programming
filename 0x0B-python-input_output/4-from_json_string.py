#!/usr/bin/python3
"""convert files"""


def from_json_string(my_str):
    """read files from filename .txt"""
    import json
    return json.load(my_str)
