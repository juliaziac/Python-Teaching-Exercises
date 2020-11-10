#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:26:11 2020

@author: JUJU
"""
########
# This program explores the probabilities of winning the "Let's Make a Deal" game from the classic Monty Hall problem. There are three doors: one with a car (the prize) behind it, and two with goats behind them. The player must choose a door, the host then reveals a "goat" door, and then the player gets to decide if they want to keep their original choice or switch.
########


import random

def Game_Show(choice_1, choice_2):
    # This function takes two inputs: choice_1 is a door numbered 1 through 3 as the first guess, and choice_2 is if they want to keep their original door or switch after one of the goats is revealed.
    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)

    if choice_2 == 'keep':
        if doors[int(choice_1)-1] == 'goat':
            return 0
        elif doors[int(choice_1)-1] == 'car':
            return 1
    elif choice_2 == 'switch':
        if doors[int(choice_1)-1] == 'goat':
            return 1
        elif doors[int(choice_1)-1] == 'car':
            return 0

def Probability_of_Winning(switch_or_keep, number_of_games):
    wins = 0
    for i in range(number_of_games):
        wins += Game_Show(random.randint(1,3), switch_or_keep)
    print(wins/number_of_games)

# TO-DO's:
# 1. User-friendly print statement explaining probability
# 2. Make Game Show function with n doors 

