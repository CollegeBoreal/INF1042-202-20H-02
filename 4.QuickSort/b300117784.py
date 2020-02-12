# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:25:59 2020

@author: Bertrand
"""

#quicksort 

def quicksort(array):
    # Base case
    if len(array) < 2:
        return array
    else:
        # Recursive case
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([25, 65, 5, 84, 500, 250, 600, 13]))