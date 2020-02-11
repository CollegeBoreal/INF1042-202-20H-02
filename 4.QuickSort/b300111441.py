# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:16:56 2020

@author: skofo
"""

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i<= pivot] 
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([25, 5, 84, 500, 250, 600, 13]))  
  