# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:30:31 2020

@author: kdmar
"""

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
print (selections([5, 3,6, 25, 45]))


