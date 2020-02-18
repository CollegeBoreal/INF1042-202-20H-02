"""
Created on Tue Feb 11 15:28:06 2020

@author: iDIR
"""


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i<= pivot] 
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([22, 4, 84, 400, 350, 499,500, 11])) 
