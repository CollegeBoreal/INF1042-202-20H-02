# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:15:37 2020

@author: User
"""

def fact(x):
    if(x==1):
        return 1
    else:
        return x*fact(x-1)

print(fact(2))
