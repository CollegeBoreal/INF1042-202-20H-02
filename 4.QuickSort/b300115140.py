# -*- coding: utf-8 -*-
"""
Quick sort exercice
"""

def quicksort(array):  
    if len(array) < 2:    
        return array         
    else:   
        pivot = array[0]        
        less = [i for i in array[1:] if i <= pivot]   
        greater = [i for i in array[1:] if i > pivot]             
        return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort ([2,3,9,40,4]))


