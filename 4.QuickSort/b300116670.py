# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:20:03 2020

@author: kdmar
"""

def quicksort(array):
    
    #base case
    if len(array) < 2:
        return array
    
    else:
        #recursive case
        pivot   = array[0]
        less    = [i for i in array[1:] if i <= pivot] #(1:) permet de selectionner seulement le terme 1 et le reste.
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less ) + [pivot] + quicksort(greater)
    
print(quicksort([25,65,5,84,500,250,600,13]))