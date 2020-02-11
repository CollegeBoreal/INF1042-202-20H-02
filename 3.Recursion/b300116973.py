# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 13:53:27 2020

@author: dell
"""

def fact(x) :
    if x== 1:
        return 1
    else:
        return x * fact (x-1)
    
print (fact(5))