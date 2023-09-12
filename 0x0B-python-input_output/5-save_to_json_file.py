#!/usr/bin/python3
"""convert files"""


def save_to_json_file(my_obj, filename):
    """read files from filename .txt"""
    import json
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
