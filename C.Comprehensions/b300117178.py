# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:11:55 2020

@author: willfrid boris
"""
def rightTriangle(max):

   x=[(a,b,c) for c in range(11) for a in range(1,c)  for b in range (1,a) if (a**2+b**2==c**2) and (a+b+c==24)]

   return (x)

print(rightTriangle(24))