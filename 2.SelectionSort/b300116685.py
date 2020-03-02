# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 18:58:20 2020

@author: Amir
"""

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