#!/usr/bin/python3
for char in range(0, 99):
    if char > 9:
        print("{ch:02}".format(ch=char), end=", ")
print("99")
