#!/usr/bin/env python2.7
# Particle.py
# Thomas Boser

"""
Note to self: particle printing format
particle barcode, [ vertex x,y,z], [ momentum p, theta, phi ], charge
4509578221846528, [-0.0224014, -0.00570905, -51.0684], [1450.18, 2.06558, -2.19591], 1
"""

from __future__ import print_function, division

import random
import math
import Hit as gh
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Particle:
    """ particle constructor """
    def __init__(self, barcode):
        self.barcode = barcode
        self.vertices = [0, 0] #we will assume particle originates from (0, 0)

        self.hits = []
        self.hitbcs = []

    def addHit(self, hit):
        """ add a hit to self.hits """
        if hit not in self.hits: 
            self.hits.append(hit)
            self.hitbcs.append(hit.hbc)

    def plotOrigin(self):
        """ plot the origin point for the particle """
        plt.scatter(self.vertices[0], self.vertices[1], c='r')


    def plotJoins(self):
        """ plot all hits joined by a line """
        col = random.choice('bgrcmyk') #chose random color
        #self.hits.sort(key=lambda x: x.detpos)
        origin = self.vertices
        for hit in self.hits:
            plt.plot((origin[0], hit.lhit[0]),
                     (origin[1], hit.lhit[1]),
                      color = col)
            origin = hit.lhit

    def plotHits(self):
        """ plot all hits in self.hits """
        for hit in self.hits:
            hit.plotHit()

    def printHits(self):
        """ print hits to stdout """
        for hit in self.hits:
            hit.printHit()


