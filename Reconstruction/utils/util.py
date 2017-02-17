#!/usr/bin/env python2.7
# util.py
# Thomas Boser

"""
storage for utility functions used in many files
"""

from math import sqrt

def pt_dist(p1, p2): 
    """ distance between two points described by a list """
    return sqrt(abs((p1[0] - p2[0])**2) + abs((p1[1] - p2[1])**2))

def circ_intersect(v0, v1, r0, r1):
    """ return intersection points of two circles """
    dist = pt_dist(v0, v1) #calculate distance between 
    if dist > (r0 + r1): return False #out of range
    if dist < abs(r0 - r1): return False #circle contained
    if dist == 0: return False #same origin

    a = (r0**2 - r1**2 + dist**2) / (2*dist)
    b = dist - a
    h = sqrt(r0**2 - a**2)

    v2x = v0[0] + a*(v1[0] - v0[0])/dist
    v2y = v0[1] + a*(v1[1] - v0[1])/dist
    
    x3p = v2x + h*(v1[1] - v0[1])/dist
    y3p = v2y - h*(v1[0] - v0[0])/dist
    x3n = v2x - h*(v1[1] - v0[1])/dist
    y3n = v2y + h*(v1[0] - v0[0])/dist

    return [[x3p, y3p], [x3n, y3n]]
