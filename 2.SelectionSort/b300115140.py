# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:41:55 2020

@author: zacks
"""
# tri de selection exercie github 2

def findSmallest(arr):
        smallest = arr[0]
        smallest_index = 0
        for i in range(1, len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_index = i
        return smallest_index

def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
      smallest = findSmallest(arr)
      newArr.append(arr.pop(smallest))
  return newArr
print (selectionSort([523, 34, 62, 2567890, 14560]))








    
    
        
        
    
    
