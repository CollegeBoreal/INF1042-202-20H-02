#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:08:01 2020

@author: zoureni
"""

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
print(fact(6))