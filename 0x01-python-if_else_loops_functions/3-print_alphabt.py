#!/usr/bin/python3
for char in range(97, 123):
    if char not in [101, 113]:
        print("{cha:c}".format(cha=char), end="")
