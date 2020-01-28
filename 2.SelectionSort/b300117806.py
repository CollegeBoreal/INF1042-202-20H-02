# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 13:49:45 2020

@author: User
"""

# tri de selection exercie github 2

def findSmallest(arr):
        Smallest = arr[0]
        Smallest_index = 0
        for i in range(1, len(arr)):
            if arr[i] < Smallest:
                Smallest = arr[i]
                Smallest_index = i
        return Smallest_index

def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
      Smallest = findSmallest(arr)
      newArr.append(arr.pop(Smallest))
  return newArr
print (selectionSort([648, 45, 89, 347989, 24780]))