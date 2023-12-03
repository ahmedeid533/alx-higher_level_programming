#!/usr/bin/python3
"""get page"""


if __name__ == "__main__":
    from requests import post
    from sys import argv

    page = post(argv[1], data={'email': argv[2]})
    print(page.text)
