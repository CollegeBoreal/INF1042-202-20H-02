# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:08:16 2020

@author: dell
"""

t=map (lambda x:x*x, range (10))
print (list(t))



import functools 

print (functools.reduce (lambda x, y: x + y, range (10)))


