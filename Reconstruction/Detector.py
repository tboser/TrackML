#!/usr/bin/env python2.7
# Detector.py
# Thomas Boser

from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Detector:
    """ detector constructor """
    def __init__(self, radius):
        self.center = np.array([0, 0]) #2d vector, origin center assumption
        self.radius = radius

    #override equals and not equals operators to prevent duplicate detectors
    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return not self.__eq__(other)

    def plotDetector(self):
        """ plot a detector (circle) to plt figure """
        ax = plt.gca()
        ax.add_patch(patches.Circle((self.center[0], 
                                     self.center[1]),
                                     self.radius,
                                     fill = False))

    def printDetector(self):
        """ print detector information to stdout """
        print("Center = ", self.center,", radius = ", self.radius, sep='')