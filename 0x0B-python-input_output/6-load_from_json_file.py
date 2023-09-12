#!/usr/bin/python3
"""load_from_json_file"""


def load_from_json_file(filename):
    """read files from filename .txt"""
    import json
    with open(filename) as f:
        return json.load(f)
