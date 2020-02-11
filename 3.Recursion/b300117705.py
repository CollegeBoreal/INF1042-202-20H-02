# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:12:42 2020

@author: acorl
"""


def fact(l):
    if l == 0:
        return 1
    else:
        return l * fact(l - 1)
print (fact(5))    
