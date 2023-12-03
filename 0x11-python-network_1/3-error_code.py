#!/usr/bin/python3
"""get error"""


if __name__ == "__main__":
    from urllib.request import urlopen
    from urllib.error import HTTPError
    from sys import argv

    try:
        with urlopen(argv[1]) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as err:
        print('Error code:', err.code)