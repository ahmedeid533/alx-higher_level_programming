#!/usr/bin/python3
"""read files"""


def write_file(filename="", text=""):
    """read files from filename .txt"""
    with open(filename, 'w',encoding="utf-8") as f:
        return f.write(text)
