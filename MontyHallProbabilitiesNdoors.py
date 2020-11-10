#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:26:11 2020

@author: JUJU
"""
########
# This program explores the probabilities of winning the "Let's Make a Deal" game from the classic Monty Hall problem, but with N doors. There are three or more doors: one with a car (the prize) behind it, and the rest with goats behind them. The player must choose a door, the host then reveals a "goat" door, and then the player gets to decide if they want to keep their original door choice or switch.
########


import random

def Game_Show_N_Doors(choice_1, choice_2, N):
    # This function takes two inputs: choice_1 is a door numbered 1 through N as the first guess, choice_2 is if they want to keep their original door or switch after one of the goats is revealed, and N is the number of doors (which must be at least 3). If they choose to switch doors, it reveals the smallest number door with a goat behind it (as long as that wasn't their original choice) and switches to a random door, guaranteed NOT to be their original choice or the revealed door.
    doors = ['car'] + (N-1)*['goat']
    random.shuffle(doors)

    if choice_2 == 'keep':
        if doors[choice_1-1] == 'goat':
            return 0
        elif doors[choice_1-1] == 'car':
            return 1
    elif choice_2 == 'switch':
        doors[choice_1-1] = 'not an option'
        doors[doors.index('goat')] = 'not an option' # This reveals the first door with a goat which isn't their original door choice.
        x = choice_1
        while doors[x-1] == 'not an option': # This guarantees the random new door is not the original door or the revealed door.
            x = random.randint(1, N)
        if doors[x-1] == 'goat':
            return 0
        elif doors[x-1] == 'car':
            return 1

def Probability_of_Winning(switch_or_keep, number_of_games, N):
    # Shows the probability of winning with just one choice to switch or keep with N doors.
    # The probability of winning when you keep your first door choice is 1/N.
    # The probability of winning when you switch your first door choice and only get to switch once is (N-1)/(N^2-2N). This is because the probability = the probability of choosing the right door with the new limited options (you can't choose your original door and you can't choose the revealed door, so you can only choose 1 from (N-2) doors) AND (so multiply these two probabilities) the probability your first door choice was wrong (which is (N-1)/N, because your chance of choosing the right door initially was 1/N and this expression is on 1 - 1/N).
    wins = 0
    for i in range(number_of_games):
        wins += Game_Show_N_Doors(random.randint(1,N), switch_or_keep, N)
    return(wins/number_of_games)

def Number_of_Wins(switch_or_keep, number_of_games, N):
    # This computes how many times you will win depending on your choice to switch or keep your original door choice with N doors for number_of_games trials.
    # This makes the Should_You_Always_Switch function slightly more accurate than when using Probability_of_Winning, becuase you subtract the wins first THEN divide by the number of trials.
    wins = 0
    for i in range(number_of_games):
        wins += Game_Show_N_Doors(random.randint(1,N), switch_or_keep, N)
    return(wins)

def Should_You_Always_Switch(number_of_games, N):
    # This calculates how much greater your probability of winning is if you choose to switch just once with N doors.
    # The answer should converge to (N-1)/(N^2-2N) - 1/N expressed as a percent.
    print ('You have about a', str(100*(Number_of_Wins('switch', number_of_games, N)-Number_of_Wins('keep', number_of_games, N))/number_of_games), 'percent greater chance of winning when you choose to switch doors just one time in the game with', str(N), 'doors.')

