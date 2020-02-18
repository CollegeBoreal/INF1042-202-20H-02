# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:04:43 2020

@author: User
"""


def rightTriangle(max):
    
   l = [(a,b,c)
   for c in range( 1, 11)
       
   for a in range(1, c + 1 )
   
   for b in range(1, a + 1)
                  
   if a**2 + b**2==c**2 and a + b + c ==24]
       
   return l

print(rightTriangle(24))