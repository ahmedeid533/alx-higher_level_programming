#!/usr/bin/python3
"""get the email"""


if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    from sys import argv

    dic = {"email": argv[2]}
    req = Request(
            argv[1], urlencode(dic).encode("ascii"))
    with urlopen(req) as res:
        print(res.read().decode('utf-8'))
