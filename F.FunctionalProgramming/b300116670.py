# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:33:03 2020

@author: kdmar
"""



a = [x for x in range (10)]
print(a)


s = [2*x for x in range(10)]
print(s)


j = [x for x in range(10) if x % 2 == 0]
print(j)


g =  [x for x in range(10) if x % 2 != 0 ]