# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:20:15 2020

@author: User
"""

def quicksort(array):
    # base case
    if len(array) < 2 :
        return array
    else:
        # recursive case
        pivot = array [0]
        less = [i for i in array [1:] if i <= pivot]
        greater = [i for i in array[1:] if i <= pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
print(quicksort([24, 50, 200, 800, 10, 45, 13, 70]))

    