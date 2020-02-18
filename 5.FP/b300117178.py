# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:10:47 2020

@author: willfrid boris
"""
import functools
t=map(lambda x:x*2,range(10))
print(list(t))
print(list(filter(lambda x:x>=5,range(20))))
print(functools.reduce(lambda x, y :x+y,range(10)))
#print(functools.reduce(lambda x,y: x*(y-1),range(1,1)))



    