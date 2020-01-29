# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:38:26 2020

@author: dell
"""

#how to write code selection sort


def trouvepetit (arr):
    petit = arr [0]
    petit_index = 0
    for i in range (1, len (arr)) :
        if arr[i] < petit:
            petit = arr [i]
            petit_index = i
    return petit_index

def selectionSort (arr):
    newArr = []
    for i in range (len(arr)):
        petit = trouvepetit (arr) 
        newArr.append(arr.pop(petit))
    return newArr

print (selectionSort([5, 1, 8, 20, 3]))