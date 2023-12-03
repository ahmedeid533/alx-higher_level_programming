#!/usr/bin/python3
"""get the header"""


if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as data:
        parse = data.headers.get('X-Request-Id')
        print(parse)
