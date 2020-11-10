#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 22:43:37 2020

@author: JUJU
"""

# Deitel Problem 4.12
# The Tortoise and the Hare race with a random number twist.

import random
import time

def tortoise():
    # Determines how much the tortoise will move.
    T_move = random.randint(0,10)
    if T_move <= 4:
        return 3
    elif T_move in [5, 6]:
        return -6
    else:
        return 1
    
def hare():
    # Determines how much the hare will move.
    H_move = random.randint(0,10)
    if H_move <= 1:
        return 0
    elif H_move in [2, 3]:
        return 9
    elif H_move == 4:
        return -12
    elif H_move in [5, 6, 7]:
        return 1
    else:
        return -2

def track():
    # Creates a blank track.
    track_list = []
    for i in range(70):
        track_list.append('-')
    return track_list
        
def show_track(track_list):
    # Displays any track.
    track_string = "".join(track_list)
    print(track_string)

def race():
    # Runs the race.
    
    # Set-Up
    print("\n")
    track_list = track()
    time.sleep(1)
    show_track(track_list)
    print("\nBANG!!!!!\n")
    time.sleep(1)
    print("AND THEY\'RE OFF!!!!!\n")
    time.sleep(1)
    
    T_position = 0
    H_position = 0
    
    while True:
        T_position += tortoise()
        H_position += hare()
        
        # Corrects for negative positions.
        if T_position < 0:
            T_position = 0
        if H_position < 0:
            H_position = 0
            
        # States winning events.
        if T_position >= 69 and H_position >= 69:
            print("It's a tie.")
            break
        elif T_position >= 69:
            print("TORTOISE WINS!!! YAY!!!")
            break
        elif H_position >= 69:
            print("Hare wins. Yuch.")
            break
        
        # Shows position of tortoise and hare on track.
        track_list[T_position] = "T"
        track_list[H_position] = "H"
        
        # Accounts for collision events.
        if T_position == H_position:
            if T_position <= 6:
                track_list[0:7] = list("OUCH!!!")
            elif T_position >= 63:
                track_list[63:70] = list("OUCH!!!")
            else:
                track_list[T_position-3:T_position+4] = list("OUCH!!!")
                
        # Shows race.
        show_track(track_list)
        print("")
        time.sleep(1)
        track_list = track()

