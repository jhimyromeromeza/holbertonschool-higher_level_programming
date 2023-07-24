#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        valor = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        valor = None
    return valor
