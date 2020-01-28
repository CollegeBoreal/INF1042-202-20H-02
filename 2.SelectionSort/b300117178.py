# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:29:04 2020

@author: willfrid boris
"""

def selectionSort(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if(arr[i]>arr[j]):
                g=arr[j]
                arr[j]=arr[i]
                arr[i]=g
    return arr
print(selectionSort([4,8,2,6,3,9]))
print(selectionSort([9,8,2,2,3,4]))