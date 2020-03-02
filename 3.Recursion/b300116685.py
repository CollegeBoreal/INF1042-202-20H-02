# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 19:06:05 2020

@author: Amir
"""

def fact(x) :
    if x== 1:
        return 1
    else:
        return x * fact (x-1)
    
print (fact(5))