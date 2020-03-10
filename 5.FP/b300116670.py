# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 12:40:52 2020

@author: kdmar
"""

t=map (lambda x:x*x, range (10))
print (list(t))



import functools 

print (functools.reduce (lambda x, y: x + y, range (10)))