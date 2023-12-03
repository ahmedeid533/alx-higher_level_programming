#!/usr/bin/python3
""" fetch url """


if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as data:
        parse = data.read()
        print("Body response:")
        print("\t- type: {}".format(type(parse)))
        print("\t- content: {}".format(parse))
        print("\t- utf8 content: {}".format(parse.decode('utf-8')))
