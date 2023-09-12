#!/usr/bin/python3
"""read files"""


def read_file(filename=""):
    """read files from filename .txt"""
    read_data = ""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    print(read_data, end="")
