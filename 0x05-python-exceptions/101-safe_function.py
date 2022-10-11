#!/usr/bin/python3

def safe_function(fct, *args):
    import sys
    try:
        if fct:
            return (fct(*args))
    except (ValueError, TypeError, NameError,
            IndexError, ZeroDivisionError) as err:
        print("Exception:", err, file=sys.stderr)
        return (None)
