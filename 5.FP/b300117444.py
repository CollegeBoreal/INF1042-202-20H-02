# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:28:06 2020

@author: iDIR
"""

# Ecrire Un programme qui utilise map avec une fonction anonyme
#avec un generateur allant jusqyu'a 10


w=map(lambda x: x * 2,range(10))

print(list(w))

# Filter

filter(lambda x: x >= 5, range(20))

list(filter(lambda x: x >= 5, range(20)))


#Reduction

import functools

functools.reduce(lambda x,y: x + y,range(10))
