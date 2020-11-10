#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:26:11 2020

@author: JUJU
"""
########
# This program allows players to play the most simple version of the "Let's Make a Deal" game from the classic Monty Hall problem. There are three doors: one with a car (the prize) behind it, and two with goats behind them. The player must choose a door, the host then reveals a "goat" door, and then the player gets to decide if they want to keep their original choice or switch.
########


import random

def GameShow():
    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)
    doors_check = doors[:]

    choice_1 = input('Welcome to Let\'s Make a Deal! \n\nBehind one of these doors is a car, which is yours to win \nif you make the correct choice! Behind the other two are \ngoats. \n\nSo what will it be, door 1, 2, or 3? (type the number) \n\n')


    doors[int(choice_1)-1] = 'chosen'
    guaranteed_goat = doors.index('goat')
    choice_2 = input('\nYou\'ve chosen door ' + choice_1 + ', so we\'ll reveal that door ' + str(guaranteed_goat+1) + ' is a \ngoat! \n\nWill you keep your original guess, door ' + choice_1 + ' or switch doors? (type \nkeep or switch) \n\n')

    if choice_2 == 'keep':
        if doors_check[int(choice_1)-1] == 'goat':
            print('\nAh, that\'s the goat. Better luck next time! \n')
        elif doors_check[int(choice_1)-1] == 'car':
            print('\nYou won the car! \n')
    elif choice_2 == 'switch':
        if doors_check[int(choice_1)-1] == 'goat':
            print('\nYou won the car! \n')
        elif doors_check[int(choice_1)-1] == 'car':
            print('\nAh, that\'s the goat. Better luck next time! \n')



# TO-DO's:
# 1. Outside this function make a win count
# 2. Explore textwrap library
# 3. Make a 'play again' option
# 4. Modify choice_1 to accept 1 or one, etc.
# 5. Modify choice_2 to say which door number you're switching to
# 6. Modify choice_2 to accept 'k', 's', or a door number

