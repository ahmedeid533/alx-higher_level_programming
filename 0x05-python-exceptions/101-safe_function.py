#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as exp:
        import sys
        print("Exception: {}".format(exp), file=sys.stderr)
        return None
