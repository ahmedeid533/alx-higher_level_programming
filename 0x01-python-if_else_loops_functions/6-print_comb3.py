#!/usr/bin/python3
for i in range(8):
    for j in range(i+1, 10):
        print("{i2}{j2}".format(i2=i, j2=j), end=", ")
print("89")
