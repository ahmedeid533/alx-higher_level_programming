#!/usr/bin/python3
"""get url again"""


if __name__ == "__main__":
    from requests import get

    page = get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print("\t- type: {}".format(page.text.__class__))
    print("\t- content: {}".format(page.text))
