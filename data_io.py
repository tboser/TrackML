#!/usr/bin/env python2.7
# data_io.py
# Thomas Boser

from __future__ import print_function

def printv(verbose, *args): #written to mimic python3 print
    """ toggleable print """
    if verbose:
        for arg in args:
            print(arg, end="")
        print()
