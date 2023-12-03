#!/usr/bin/python3
"""parse json"""


if __name__ == "__main__":
    from requests import post
    from sys import argv

    query = argv[1] if len(argv) > 1 else ""
    req = post('http://0.0.0.0:5000/search_user', data={'q': query})
    try:
        res = req.json()
        if res == {}:
            print('No result')
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print('Not a valid JSON')
