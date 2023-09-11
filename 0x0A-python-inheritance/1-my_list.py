#!/usr/bin/python3
"""sort list"""


class MyList(list):
    """list class."""

    def print_sorted(self):
        """Print the sorted list"""
        print(sorted(self))
