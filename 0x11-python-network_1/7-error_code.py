#!/usr/bin/python3
"""get res state"""


if __name__ == "__main__":
    from requests import get
    from sys import argv

    res = get(argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
