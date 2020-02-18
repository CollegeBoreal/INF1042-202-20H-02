# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:28:06 2020

@author: iDIR
"""

import functools
t=map(lambda x:x*2,range(10))

print(list(t))

print(list(filter(lambda x:x>=5,range(20))))

print(functools.reduce(lambda x, y :x+y,range(10)))

