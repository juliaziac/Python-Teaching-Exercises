#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 19:35:14 2020

@author: JUJU
"""

# msdie.py from Zelle Ch. 10
#    Class definition for an n-sided die.

from random import randrange

class MSDie:

    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randrange(1, self.sides+1)

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value  
        

# My testing

die = MSDie(6)
print(die.getValue())
die.roll()
print(die.getValue())