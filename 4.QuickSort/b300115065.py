# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:17:14 2020
@author: fadde
"""

def quicksort (array) :
    
    if len(array) < 2 :
        
        return array
    
    else :
        pivot = array [0]

        less = [i for i in array [1:] if i <= pivot]
        
        greater = [i for i in array [1:] if i > pivot]
        
        return quicksort (less ) + [pivot] + quicksort (greater) 

print (quicksort ([25, 65, 500, 250, 600, 13]))    
