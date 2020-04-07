# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 15:13:03 2020

@author: idira
"""

def rightTriangle (max):

    rightTriangle = [(a, b, c)
#Expression
    for c in range (1, 11)
    for a in range (1, c)
    for b in range (1, a)

     if a**2 + b**2 == c**2 and  a + b + c == 24]
#valeur

    return rightTriangle
print (rightTriangle(24))
