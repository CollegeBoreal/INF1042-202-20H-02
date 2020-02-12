# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:30:36 2020

@author: User
"""

f = map ( lambda x : x * 2 ,range ( 16 ))

print ( list( f))

#filtre
filter ( lambda x: x >= 5 , range ( 20 ))

list(filter( lambda x: x >= 5 , range ( 20)))

#reduice

import functools

functools . reduce ( lambda x, y : x + y, range ( 10 ))
