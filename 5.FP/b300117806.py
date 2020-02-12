# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:31:20 2020

@author: User
"""

h=map (lambda x: x * 2, range (10))

#filter
print (list(h))

filter ( lambda x: x >= 5 , range (15))

list(filter(lambda x: x >= 5 , range(15)))

 #reduce
  
import functools

functools.reduce(lambda x,y: x + y, range(10))

  
