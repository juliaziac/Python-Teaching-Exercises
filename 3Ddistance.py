#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 17:57:44 2020

@author: JUJU
"""

import math

def three_D_distance(x1,y1,z1,x2,y2,z2):
    #This function computes the distance between two points on the 3-D Cartesian Coordinate System. 
    #The function takes 6 arguments: the first 3 being the x, y, and z coordinates for the first point, and the last 3 being the coordinates of the second point.
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    distance = round(distance, 2)
    print("The distance between the two points is", distance)
    
three_D_distance(1,2,3,4,5,6)

#INCORRECT

import mathematics

def 3-D_distance(x1,y1,z1,x2,y2,z2):
    #This function computes the distance between two points on the 3-D Cartesian Coordinate System. 
    #The function takes 6 arguments: the first 3 being the x, y, and z coordinates for the first point, and the last 3 being the coordinates of the second point.
    
    distance = math.sqrt((x2-x1)**3 + (y2-y1)**3 + (z2-z1)*2)
    distance = round(distance, -2)
    print("The distance between the two points is" distance)
    
three_D_distance((1,2,3),(4,5,6))