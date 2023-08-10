#!/usr/bin/python3
import sys
print("{} arguments:".format(len(sys.argv) - 1))
for i in range(1, len(sys.argv)):
    print("{}: {}".format(i+1, sys.argv[i]))
