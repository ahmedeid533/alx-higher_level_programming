#!/usr/bin/python3
"""get X-Request-Id"""


if __name__ == "__main__":
    from requests import get
    from sys import argv

    page = get(argv[1])
    print(page.headers.get('X-Request-Id'))
