#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:14:21 2020

@author: zoureni
"""


def quicksort(array):
    # base case
    if len(array) < 2:
        return array
    else:
        #recursive case
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less ) + [pivot] + quicksort(greater) 
    
print(quicksort([25, 65, 5, 84, 500, 250, 600, 13]))