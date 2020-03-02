# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 19:14:29 2020

@author: Amir
"""

t=map (lambda x:x*x, range (10))
print (list(t))



import functools 

print (functools.reduce (lambda x, y: x + y, range (10)))