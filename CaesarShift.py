#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 22:29:51 2020

@author: JUJU
"""


#Removes spaces and puctuation, and changes all letters to lowercase.

def Just_Letters(original_message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    just_letters_message = "" #Starts with a blank message.
    
    for letter in original_message.lower(): #.lower() changes all characters to lowercase.
        if alphabet.find(letter) == -1:
            just_letters_message += "" #Removes spaces and puctuation. Make this += letter if you want to keep the spaces and puctuation.
        else:
            just_letters_message += letter
            
    return just_letters_message

###########################

#Caesar Shift, use Just_Letters first

def Caesar_Shift(original_message, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded_message = "" #Starts with a blank message.
    
    for letter in original_message:
        encoded_message += alphabet[(alphabet.find(letter)+shift)%26] #Shifts each letter, and the %26 makes the shift work even if it must wrap around past z.
        
    return encoded_message
    
############################

#Vigenere Cipher, use Just_Letters first for both the message and the keyword

def Vigenere_Cipher(original_message, keyword):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded_message = "" #Starts with a blank message.
    
    #Make a keyword string the same length as the original message (without spaces or puctuation).
    keyword_match_message_length = ""
    for i in range(len(original_message)):
        keyword_match_message_length += keyword[i%len(keyword)]
        
    #Now do the Caesar shift for each letter based on the corresponding keyword letter shift.
    for i in range(len(original_message)):
        shift = alphabet.index(keyword_match_message_length[i])
        encoded_message += Caesar_Shift(original_message[i], shift)
        
    return encoded_message




    