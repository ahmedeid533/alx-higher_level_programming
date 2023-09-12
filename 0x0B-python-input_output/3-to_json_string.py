#!/usr/bin/python3
"""convert files"""


def to_json_string(my_obj):
    """read files from filename .txt"""
    import json
    return json.dumps(my_obj)
