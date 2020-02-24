# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:26:59 2020

@author: Amir
"""


def binary_search(list,items):
    ValeurMini = 0
    ValeurMaxi = len(ma_liste)-1
    
    
    while ValeurMini <= ValeurMaxi:
        mid= (ValeurMini + ValeurMaxi)//2
        guess = list[mid]
        if guess == article :
           return mid
        if guess > article:
           ValeurMaxi = mid - 1
        else:
            ValeurMini = mid + 1
    return None 



ma_liste = [1,7,11,14,19,20,25]


print (binary_search(ma_liste, 7))
print (binary_search(ma_liste, 20))
print (binary_search(ma_liste, 21))
