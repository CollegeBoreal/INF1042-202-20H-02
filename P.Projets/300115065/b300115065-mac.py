# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 13:55:45 2020

@author: akram fadde
"""

# Code Morse

from time import sleep
# from winsound import Beep
import pygame

def Beep(a,b):
  sounda= pygame.mixer.Sound("./sounds/AMFMBEEP.wav")
  sounda.play()

pygame.init()
pygame.mixer.init()

freq = 760          # frÃ©quence de la note
point = 0.21        # durÃ©e du point
trait = point * 3   # durÃ©e du trait
blanc = point * 4   # durÃ©e du blanc

CODE = {' ': ' ',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ',': '--..--',
        '.': '.-.-.-',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..'}


def coder(phrase):
    # code une string avec des traits, des points et des blancs
    morse = []
    phrase = phrase.upper()
    for c in phrase:
        if c in CODE.keys():
            morse.append(CODE[c])
    print(morse)
    return morse

def sonoriser(morse):
    # transforme le code Morse en une sÃ©rie de durÃ©es
    son=[]
    for mot in morse:
        for s in mot:
            if s=='.':
                son.append(point)
            elif s=='-':
                son.append(trait)
            else:
                son.append(blanc)
        son.append(blanc)
    return son

def jouer(morse):
    # beepe les durÃ©es lues
    for t in morse:
        if t==blanc:
            sleep(t)
        else:
            Beep(freq,round(t*1000))
            sleep(0.1)
            

phrase = input("entrÃ©e : ")
while phrase != '':
    codage=coder(phrase)
    morse = sonoriser(codage)
    jouer(morse)
    phrase = input("entrÃ©e : ")

