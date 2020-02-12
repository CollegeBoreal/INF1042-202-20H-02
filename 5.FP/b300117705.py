# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:42:23 2020

@author: acorl
"""

a = list ( map( lambda x: x * 2 , range(10)))
print(a)


b = list ( filter( lambda x: x >= 5 , range(20)))
print(b)


import functools

g = functools.reduce( lambda x, y : x +y , range(10))
print(g)