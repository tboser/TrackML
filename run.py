#!/usr/bin/env python2.7
# run.py
# Thomas Boser

"""
usage = python2.7 run.py infile outfile
"""

from __future__ import print_function

import os
import sys
import time
import particleController as pc
from data_io import printv

from __future__ import print_function

start = time.time()

#default verbose = True
verbose = True 

#main
if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("usage: python2.7 run.py infile outfile")
        exit(1)

    infilen = sys.argv[1]
    outfilen = sys.argv[2]

    #try to read from infile
    printv(verbose, "opening infile")
    try:
        infile = open(infilen, 'r')
    except IOError:
        print("infile could not be opened")
        exit(1)
  
    #initialize particlecontroller  
    cont = pc.particleController()

    #add hits from infile to particlecontroller
    for line in infile:
        line = line.replace(']','').replace('[','')\
            .replace(' ','').rstrip().split(',')
        cont.addHit(line[0], [float(line[2]), float(line[3])], line[1])
    printv(verbose, len(cont.hits)," hits added to controller")

    printv(verbose, "creating detectors, calculating detector interceptions")
    for i in range(1000, 8001, 1000): cont.addDetector(i) #can change detector params, ex here

    cont.compHitdet() #assign detector to hits
    cont.predictParticles()

    cont.printSoln()
