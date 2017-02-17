#!/usr/bin/env python2.7
# oogenerateEvents.py
# Thomas Boser

from __future__ import print_function, division

import random
import matplotlib.pyplot as plt
import oogenerateParticles as gp
import oogenerateDetectors as gd

from math import sqrt

class Event:
    """ controller class for particles, hits, and detectors of a single event """
    def __init__(self, eventid, detrad):
        """ event constructor """
        self.eventid = eventid
        self.pbc = []
        self.hbc = []

        self.particles = []
        self.hits = []
        self.detectors = []
        for rad in detrad: self.addDetector(rad) #create detectors

        #weird way to track plot state, i'm sure there is a better way to do this
        self.plotState = []

    ##############################################################################
    ##################          PARTICLE METHODS          ########################
    ##############################################################################
    def clearParticles(self):
        """ delete every particle in self.particles """
        self.particles[:] = []

    def createParticles(self, n):
        """ add n particles to self.particles, increment bcTracker """
        if len(self.detectors) == 0:
            print("Please generate detectors before generating particles")
            return
        p_ind = len(self.pbc)
        h_ind = len(self.hbc)
        self.generateBarcodes(n) #generate n random barcodes.
        tl = len(self.detectors)
        for i in range(n):
            self.particles.append(gp.Particle(self.pbc[p_ind+i], 
                                  self.hbc[h_ind+(tl*i):h_ind+(tl*i)+tl],
                                  self.eventid))

    def printParticles(self):
        """ print all particles in self.particles to stdout """
        for partc in self.particles:
            partc.printParticle()

    def printnumParticles(self):
        """ print number of particles initialized """
        print("There are", len(self.particles), "particles.")

    def printTruths(self):
        """ prints ground truth to stdout """
        for particle in self.particles:
            particle.printTruth()

    def printSolutions(self, yetkin = False):
        """ prints solution to stdout """
        for particle in self.particles:
            particle.printSolution(yetkin)

    ##############################################################################
    ##################             HIT METHODS            ########################
    ##############################################################################
    def computeallHits(self, recompute = False):
        """ compute hits for all particles """
        for particle in self.particles:
            particle.getHits(self.detectors, recompute)

    def printallHits(self, dataset = False):
        """ print all hits in self.hits to stdout """
        if len(self.hits) == 0: self.moveHits()
        for hit in self.hits:
            hit.printHit(dataset)

    def printnumHits(self):
        """ print number of computed hits """
        print("There are", len(self.hits), "hits.")

    def clearHits(self):
        self.hits[:] = []

    ##############################################################################
    ##################          DETECTOR METHODS          ########################
    ##############################################################################
    def addDetector(self, r):
        """ add detector of radius r to self.detectors """
        if gd.Detector(r) not in self.detectors: #prevent duplicate detectors
            self.detectors.append(gd.Detector(r))

    def clearDetectors(self):
        """delete every detector in self.detectors """
        self.detectors[:] = []

    def printDetectors(self):
        """ print all detectors in self.detectors to stdout """
        for det in self.detectors:
            det.printDetector()

    def printnumDetectors(self):
        """ print number of initialized detectors """
        print("There are", len(self.detectors), "detectors.")

    ##############################################################################
    ##################           PLOTTING METHODS         ########################
    ##############################################################################
    def plotParticle_joins(self):
        """ plots line between points """
        if self._plotParticle_joins not in self.plotState:
            self.plotState.append(self._plotParticle_joins)
        self.showPlot()

    def plotParticle_origins(self):
        """ plot all particle origins """
        if self._plotParticle_origins not in self.plotState:
            self.plotState.append(self._plotParticle_origins)
        self.showPlot()

    def plotParticle_hits(self):
        """ plot all particle hits in self.particles.hits """
        if self._plotParticle_hits not in self.plotState:
            self.plotState.append(self._plotParticle_hits)
        self.showPlot()

    def plotallHits(self):
        """ plot all particle hits in self.hits """
        if self._plotallHits not in self.plotState:
            self.plotState.append(self._plotallHits)
        self.showPlot()

    def plotDetectors(self):
        """ plot all detectors """
        if self._plotDetectors not in self.plotState:
            self.plotState.append(self._plotDetectors)
        self.showPlot()

    def clearPlot(self):
        """ clear plot """
        self.plotState[:] = []

    ##############################################################################
    ##################            HELPER METHODS          ########################
    ##############################################################################
    def clearController(self):
        """ clear controller of all values """
        self.clearDetectors()
        self.clearParticles()
        self.clearPlot()
        self.clearHits()

    def moveHits(self):
        """ move hits from particles to particlecontroller after computing """
        self.clearHits()
        for particle in self.particles:
            self.hits.extend(particle.hits)

    def generateBarcodes(self, n):
        #particles will be assigned a barcode at index i and particle
        #barcodes from indices len(self.detectors)*i through 
        #len(self.detectors)*i + len(self.detectors) -1
        p_min = 1
        h_min = 1
        h_inc = len(self.detectors)

        if (self.pbc): #if there are already barcodes
            p_min = max(self.pbc) + 1
            h_min = max(self.hbc) + 1

        new_pbc = range(p_min, p_min+(n), 1)
        new_hbc = range(h_min, h_min+(h_inc*n), 1)

        random.shuffle(new_pbc)
        random.shuffle(new_hbc) # shuffle hbc and pbc for randomized barcodes

        self.pbc.extend(new_pbc)
        self.hbc.extend(new_hbc)

    def _plotParticle_origins(self):
        """ actually plots all particle origins, prevents recursion """
        for particle in self.particles:
            particle.plotOrigin()

    def _plotParticle_joins(self):
        """ actually plots line between points """
        for particle in self.particles:
            particle.plotJoins()

    def _plotallHits(self):
        """ actually plots all particle hits in self.hits, prevents recursion """
        for hit in self.hits:
            hit.plotHit()

    def _plotParticle_hits(self):
        """ actually plots all particle hits, prevents recursion """
        for particle in self.particles:
            particle.plotHits()

    def _plotDetectors(self):
        """ actually plots all detectors """
        for detector in self.detectors:
            detector.plotDetector()

    def showPlot(self):
        """ helper command to create new plot with commands used """
        for command in self.plotState: command()
        plt.scatter(0, 0, c='g') #always plot origin in green
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()

