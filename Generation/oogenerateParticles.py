#!/usr/bin/env python2.7
# oogenerateParticles.py
# Thomas Boser

"""
Note to self: particle printing format
particle barcode, [ vertex x,y,z], [ momentum p, theta, phi ], charge
4509578221846528, [-0.0224014, -0.00570905, -51.0684], [1450.18, 2.06558, -2.19591], 1
"""

from __future__ import print_function, division

import random
import math
import oogenerateHits as gh
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from utils.util import pt_dist, circ_intersect

class Particle:
    """ particle constructor """
    def __init__(self, barcode, hitbcs, eventid):
        self.barcode = barcode
        self.vertices = []
        self.mangle = []
        self.charge = None

        self.hits = []
        self.hitbcs = hitbcs

        self.eid = eventid

        ### FOR PARTICLE GENERATION ###
        self.p_radius = 0
        self.centpt = []
        self.p_circ = None
        self.m_ray = None

        self.genParticle()

    def genParticle(self):
        """ generate values for particle """
        self.vertices = [round(random.uniform(.03, -.03),7), round(random.uniform(.03, -.03),7)\
                         ,0] #Leaving z at 0, only considering 2d space for now
        self.mangle = [round(random.uniform(15000, 4000),2), round(random.uniform(4, 0),5),\
                       round(random.uniform(4, -4),5)]
        self.charge = random.randint(-1, 1)

        #particle trajectory estimations
        magfield = 1 # we will assume the magnetic field is uniform
        if self.charge != 0: 
            self.p_radius = abs(self.mangle[0] / (self.charge * magfield))
            self.centpt = [self.vertices[0] + (self.p_radius*math.sin(self.mangle[2])),
                           self.vertices[1] + (self.p_radius*math.cos(self.mangle[2]))]

    def getHits(self, detectors, override = False):
        """ produces all hits with the detectors specified, appends them
            to self.hits, assumes particles travel in circular motion so
            this is an approximation """
        if len(self.hits) == 0 or override == True: #if hits are not yet computed
            for detpos, det in enumerate(detectors):
                poss_hits = self.getIntersects(det)
                if poss_hits is not None:
                    self.hits.append(gh.Hit(self.barcode, self.hitbcs[detpos],
                                            self.eid, poss_hits, detpos+1))

    def getIntersects(self, detector):
        """ returns intersection pts of two cirles (or a line and a circle).
            does so using custom methods. """
        m_intersect = [detector.radius*math.cos(self.mangle[0])+self.vertices[0],
                       detector.radius*math.sin(self.mangle[0])+self.vertices[1]]
        if self.charge == 0: #if charge is 0 particle travels in straight line
            return m_intersect
        else: #circle circle intersection if particle is charged
            intersects = circ_intersect(detector.center, self.centpt, 
                                             detector.radius, self.p_radius)
            if not intersects: return None
            flag = 0
            if pt_dist(intersects[1], m_intersect) < pt_dist(intersects[0], m_intersect):
                flag = 1
            return intersects[flag]


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

    def printParticle(self):
        """ print particle to stdout """
        print(self.barcode,',',self.vertices,',',self.mangle,',',self.charge, sep='')

    def printTruth(self, yetkin=False):
        """ print particle track truth """
        print(self.eid, ',', self.barcode, ',', self.charge, ',', self.mangle[2],
              ',', 0, ',', ", ".join( repr(e) for e in self.hits), sep='')

    def printSolution(self, yetkin=False):
        """ print particle solution to stdout """
        if not yetkin:
            print(self.eid, ',', ", ".join( repr(e) for e in self.hits), sep='')
        else:
            for hit in self.hits:
                print(self.eid, ',', self.barcode, ',', hit.hbc, ',', hit.lhit[0], ',',
                      hit.lhit[1], sep='')

    def printHits(self):
        """ print hits to stdout """
        for hit in self.hits:
            hit.printHit()


