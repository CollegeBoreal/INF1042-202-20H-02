# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:16:17 2020

@author: willfrid boris
"""

def quicksort(array):
    if len(array)<2:
        return array
    else:
        pivot=array[0]
        less=[i for i in array[1:] if i<=pivot]
        greater=[i for i in array[1:] if i>pivot]
        return quicksort[less]+[pivot]+quicksort[greater]
print(quicksort[5,6,2,9,10,4])
        