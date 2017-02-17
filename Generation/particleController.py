#!/usr/bin/env python2.7
# particleController.py
# Thomas Boser

from __future__ import print_function

import oogenerateEvents as ge

class particleController:
    """ 
    controller for multiple events 
    all plotting is event controlled
    """
    def __init__(self):
        """ controller constructor """
        self.eventids = [0]

        self.events = []
        self.particles = []
        self.hits = []

    ##############################################################################
    ##################            EVENT METHODS           ########################
    ##############################################################################
    def generateEvent(self, numparticles, detrad = range(1000, 8001, 1000)):
        """ generate a single event with numparticles particles """
        eventid = max(self.eventids) + 1
        self.eventids.append(eventid)
        thise = ge.Event(eventid, detrad) #create event
        thise.createParticles(numparticles)
        thise.computeallHits()
        self.events.append(thise)
        self.particles.extend(thise.particles)
        self.hits.extend(thise.hits)
        return thise

    def generateEvents(self, numevents, numparticles, detrad = range(1000, 8001, 1000)):
        """ generate numevents events with numparticles particles per event """
        for i in range(0, numevents):
            self.generateEvent(numparticles, detrad)

    ##############################################################################
    ################       DATASET GENERATION METHODS        #####################
    ##############################################################################
    def printallTruths(self):
        for event in self.events:
            event.printTruths()

    def printallSolutions(self, yetkin=False):
        for event in self.events:
            event.printSolutions(yetkin)

    def printallHits(self):
        for event in self.events:
            event.printallHits(dataset = True)