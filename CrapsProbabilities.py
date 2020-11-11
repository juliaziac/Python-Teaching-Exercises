#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 13:28:41 2020

@author: JUJU
"""

#####
# This program simulates the casino game Craps. Then figures out the probability of winning N games.
#####

import random

def craps():
    # This function returns 0 for a loss and 1 for a win.
    dice_sum = random.randint(1,6) + random.randint(1,6)
    if dice_sum in [2, 3, 12]:
        return 0
    elif dice_sum in [7, 11]:
        return 1
    else:
        initial_roll, dice_sum = dice_sum, 0
        while dice_sum not in [initial_roll, 7]:
            dice_sum = random.randint(1,6) + random.randint(1,6)
        if dice_sum == 7:
            return 0
        else:
            return 1
    
def probability_win_craps(N):
    # This function determines the probability of winning the game of Craps for N games.
    wins = 0
    for i in range(N):
        wins += craps()
    print('The probability that you will win Craps in ', N, ' games is ', wins/N, ' or, ', 100*wins/N, ' percent.')