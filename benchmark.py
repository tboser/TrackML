#!/usr/bin/env python2.7
# benchmark.py
# Thomas Boser

import Generation.particleController as pc
import time

def benchmarkPC(n):
	cont = pc.particleController()
	start = time.time()
	for i in range(1000, 8001, 1000): cont.addDetector(i)
	cont.createParticles(10000)
	end = time.time()
	print n, "particles generated in", end-start, "seconds."

	start = time.time()
	cont.computeallHits()
	end = time.time()
	print "hits for", n, "particles computed in", end-start, "seconds."

n = input("How many particles do you want to generate?: ")
benchmarkPC(n)