# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 14:04:59 2020

@author: User
"""

#imprimer de 0 a 9

a = [ x for x in range (10)]

print ( a )

#creer un liste

k = [ 2, 5, 4, 8, 15]
print ( a )

#chercher les element

k[ 0 ]

f = lambda x: x + 3
[ f( x ) for x in range ( 10 ) if x % 2 == 0 ]

g = lambda x: x % 2 == 0

k = lambda a: a

def k( a ):
    return a
k ( 4 )

map (k x: x =1 )