# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 04:43:55 2020

@author: willfrid boris
"""
def findSmallest(arr):
    smallest=arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
        if(arr[i]<smallest):
            smallest=arr[i]
            smallest_index=i
    return smallest_index

def selectionSort(arr):
    newarr=[]
    for i in range(len(arr)):
        smallest=findSmallest(arr)
        newarr.append(arr.pop(smallest))
    return newarr

print(selectionSort([7, 1, 9, 4, 8]))
    
    
            