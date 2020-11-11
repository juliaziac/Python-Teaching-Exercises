#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 09:44:40 2020

@author: JUJU
"""

# Programming Final Spring 2020: Coding Questions 

"""
21. Write a program which takes as input an integer N and then counts downwards by 3's, stopping at 0 or the smallest positive integer. For example, if the user inputs 16, the output would be: 16, 13, 10, 7, 4, 1.
"""

def Countdown_by_Threes():
    N = int(input("What number do you want to start at? "))
    while N > 0:
        print(N)
        N -= 3
        
"""
22. Write a program which takes as input any phrase and outputs that phrase in Pig Latin. Pig Latin is the made-up language which takes the first syllable of a word and puts it at the end of the word with "ay." For example, "chicken soup" would turn into "icken-chay oup-say." For the purposes of YOUR program, just take the first letter of the word and put it at the end with "ay." So in YOUR program, "chicken soup" would turn into "hicken-cay oup-say." You can choose if you want your output to include the hyphens or not.
"""

def PigLatin():
    phrase = input("Type the phrase you'd like coverted into Pig Latin: ")
    words = phrase.split()
    pig_latin_phrase = ''
    for word in words:
        word = word[1:] + word[0] + 'ay '
        pig_latin_phrase += word
    print(pig_latin_phrase)
    
"""
23. Write a program which outputs a twist on the classic school bus song: "99 bottles of boba on the wall, 99 bottles of boba. Take one down, pass it around, 98 bottles of boba on the wall. 98 bottles of boba ..." all the way down to "1 bottle of boba on the wall, 1 bottle of boba. Take one down, pass it around, no more bottles of boba on the wall."
"""

def NinetyNineBottles():
    N = 99
    while N > 2:
        print(N, "bottles of boba on the wall,", N, "bottles of boba. Take one down, pass it around,", N-1, "bottles of boba on the wall. ")
        N -= 1
    print("2 bottles of boba on the wall, 2 bottles of boba. Take one down, pass it around, 1 bottle of boba on the wall.")
    print("1 bottle of boba on the wall, 1 bottle of boba. Take one down, pass it around, no more bottles of boba on the wall.")
    
"""
24. Write a program which takes as input a year, and outputs the date of Easter that year using the following formula (recall % is the modulo operation):

a = year % 19
b = year % 4
c = year % 7
d = (19a + 24) % 30
e = (2b + 4c + 6d + 5) % 7

And then the date of Easter is March (22 + d + e). This addition could result in a day in April, so make sure to account for that. 

To check your work: Easter in 2005 was on March 27 and Easter in 2020 was on April 12.
"""
    
def Easter():
    year = int(input("What year do you want to know when Easter was? "))
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19*a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7
    date = 22 + d + e
    if date < 32:
        print("Easter was on March " + str(date) + " in the year " + str(year) +".")
    if date > 31:
        print("Easter was on April " + str(date-31) + " in the year " + str(year) +".")
    
"""
25. Write a program which takes as input the time in hours:minutes and an integer N, and returns the time in hours:minutes N hours from then. For example, if the input time is 10:30 and N = 3, your program would output "The time 3 hours from 10:30 is 1:30." 

Notes: You do NOT have to specify AM/PM unless you'd like to. You CAN express 1:30 as 01:30 if you want. You CAN use 24-hour time (so 1:30 pm would be 13:30) if you want. And you CAN write your times in military time (so 1:30 pm would be 1330 without any colon).
"""

def Time_Addition():
    time = input("What is your starting time (in hours:minutes)? ")
    N = int(input("How many hours from that time would you like know the time? "))
    if len(time) == 5:
        start_hour = int(time[0:2])
    if len(time) == 4:
        start_hour = int(time[0])
    new_hour = start_hour + N
    if new_hour > 12:
        new_hour -= 12
    new_time = str(new_hour)+time[-3:]
    print("The time", N, "hours from", time, "is", new_time)

"""
26. Write a program which performs a simulation to estimate the probability of rolling three-of-a-kind with a set of five six-sided dice. Have your simulation estimate the probability for at least 1000 rolls. Three-of-a-kind means that three of the dice match. So for example, 1, 3, 4, 4, 4 is a set with three-of-a-kind, but 5, 3, 1, 4, 2 is not and 6, 6, 2, 6, 6 is neither.
"""

import random

def Three_of_a_Kind():
    three_of_a_kind = 0
    
    for i in range(1000):
        hand = []
        for i in range(5):
            hand.append(random.randint(1,6))
        count = 0

        for die in hand:
            count = hand.count(die)
            if count == 3:
                three_of_a_kind += 1
                break
    print("The probability of rolling three-of-a-kind is", three_of_a_kind/1000)

# The answer should be 1500/6^5 which is 0.1929

"""
27. Write a program which takes as input an integer N, and calculates how far you are from your starting point in a 2-D Random Walk after N steps. For each "step" you have 4 equally-probable random choices: forward, backward, left, or right. 

Hint: If you call the forward-backward motion +1 or -1 in the y-direction, and the right-left motion +1 or -1 in the x-direction, then the distance from your starting point is given by the square root of (x ^2 + y ^2), where x is the sum of the right-left steps and y is the sum of the forward-backward steps.
"""

import random
import math

def Two_D_Random_Walk():
    N = int(input("How many steps would you like to take in your random walk? "))
    motion = ['plus_x', 'minus_x', 'plus_y', 'minus_y']
    x = 0
    y = 0
    for i in range(N):
        step = motion[random.randint(0,3)]
        if step == 'plus_x':
            x += 1
        if step == 'minus_x':
            x -= 1
        if step == 'plus_y':
            y += 1
        if step == 'minus_y':
            y -= 1
    distance = math.sqrt(x**2 + y**2)
    print("You are", distance, "steps from your starting point after a 2D random walk of", N, "steps.")

# The answer should be around sqrt(N)






























