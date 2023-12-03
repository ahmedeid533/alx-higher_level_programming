#!/usr/bin/python3
"""my github"""


if __name__ == "__main__":
    from requests import get
    from sys import argv

    req = get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(req.json().get('id'))
