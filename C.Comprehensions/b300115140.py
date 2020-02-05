# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:20:20 2020

Exercice sur ccode comprehension
"""

def rightTriangle(max):
    l = [(a, b, c)
    for c in range(1, 11)
    for a in range(1, 11)
    for b in range(1, 11)
    if a**2 + b**2 == c**2 and a + b + c == 24]
 
    return l
print (rightTriangle(24))

        
    