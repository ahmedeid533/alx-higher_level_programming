#!/usr/bin/python3
import sys
summ = 0
for i in range(1,len(sys.argv)):
    summ += int(sys.argv[i])
print(summ)