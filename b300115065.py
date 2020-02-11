"""
Created on Tue Feb 11 15:36:24 2020

@author: akram fadde
"""



def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i<= pivot] 
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10, 2, 74, 100, 210, 1000, 16]))  
