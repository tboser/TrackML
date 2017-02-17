#!/usr/bin/env python2.7
# reconstructController.py
# Thomas Boser

from __future__ import print_function

import Reconstruction.Event as e

class reconstructController:
    """ 
    Controller for track reconstruction
    """
    def __init__(self):
        """ controller constructor """
        self.eventids = []

        self.events = []
        self.particles = []
        self.hits = []

    ##############################################################################
    ###################            DATA METHODS           ########################
    ##############################################################################
    def uploadFile(self, path):
    	""" upload a file into data types """
    	pass

    ##############################################################################
    ##################       RECONSTRUCTION METHODS        #######################
    ##############################################################################



    ##############################################################################
    #######################       HELPER METHODS       ###########################
    ##############################################################################
	