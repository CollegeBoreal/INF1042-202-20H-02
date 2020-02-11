
"""
Created on Tue Jan 21 13:32:22 2020

@author: 10
"""

def TrouvPlusPetit(arr):
    
        LaPlusPetite = arr[0]
        LaPlusPetite_index = 0
        
        for i in range(1, len(arr)):
            if arr[i] < LaPlusPetite:
                LaPlusPetite = arr[i]
                LaPlusPetite_index = i
        
        return LaPlusPetite_index


def selectionSort(arr):
 
    newArr = []
 
    for i in range(len(arr)):
      smallest = TrouvPlusPetit(arr)
      newArr.append(arr.pop(smallest ))
 
    return newArr
print (selectionSort([24, 21, 11, 74, 45, 12, 19, 17]))
