# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:10:27 2020

@author: Bertrand 
"""

# Ecrire Un programme qui utilise map avec une fonction anonyme lambda (x) = x * 2
#avec un generateur allant jusqyu'a 10


w=map(lambda x: x * 2,range(10))

print(list(w))

# Filter

filter(lambda x: x >= 5, range(20))

list(filter(lambda x: x >= 5, range(20)))


#Reduce

import functools

functools.reduce(lambda x,y: x + y,range(10))