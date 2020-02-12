# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:06:27 2020

@author: Bertrand
"""

def fact(x):
    if(x==1):
        return 1
    else:
        return x*fact(x-1)

print(fact(6))