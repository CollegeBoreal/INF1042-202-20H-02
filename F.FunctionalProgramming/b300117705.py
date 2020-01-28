# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:01:47 2020

@author: acorl
"""


a = [x for x in range (10)]
print(a)

s = [2*x for x in range(10)]
print(s)

j = [x for x in range(10) if x % 2 == 0]
print(j)

g =  [x for x in range(10) if x % 2 != 0 ]