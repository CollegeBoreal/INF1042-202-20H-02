# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 13:21:17 2020

@author: skofo
"""

def rightTriangle(max):
    
    max =[ (a,b,c)
    
    for c in range(1 , 15)
    for a in range(1,c - 1) 
    for b in range(1, a - 1)  

    if a ** 2 + b ** 2 == c ** 2
    and a + b + c == 24  ]
        
    return max
    
print( rightTriangle(max) )
    