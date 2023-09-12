#!/usr/bin/python3
"""read files"""


def append_write(filename="", text=""):
    """read files from filename .txt"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
