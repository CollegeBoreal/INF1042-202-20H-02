# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:25:23 2020

@author: User
"""

def rightTriangle( max ):
    
   x=[ ( a,b,c )for c in range ( 11 ) for a in range( 11 ) for b in range( 11 ) if (a**2+b**2==c**2) and (a+b+c==24) ]
   
   return (x)

print( rightTriangle (24) )