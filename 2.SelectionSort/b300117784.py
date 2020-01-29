# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 16:15:24 2020

@author: Bertrand 
"""

# selectionSort 


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# Utilisons SelectionSort
    
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
        
    return newArr

print (selectionSort([5, 3, 6, 2, 10]))

        
    