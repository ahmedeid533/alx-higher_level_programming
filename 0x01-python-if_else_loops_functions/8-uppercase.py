#!/usr/bin/python3
def uppercase(str):
    cpy = ""
    for i in range(len(str)):
        if ord(str[i]) in range(97, 123):
            cpy += chr(ord(str[i]) - 32)
        else:
            cpy += str[i]
    print(cpy)
