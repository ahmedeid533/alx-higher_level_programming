#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("{} argument:".format(count))
    else:
        print("{} arguments:".format(count))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
