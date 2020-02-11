# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:29:20 2020

@author: User
"""

def trouve_petit(arr):
    
        smallest = arr[0]
        smallest_index = 0
        
        for i in range(1, len(arr)):
            
            if arr[i] < smallest:
                
                smallest = arr[i]
                smallest_index = i
                
        return smallest_index

def selectionSort(arr):
    
  nouveau_arr = []
  
  for i in range(len(arr)):
      
      smallest = trouve_petit (arr)
      nouveau_arr.append(arr.pop(smallest))
      
  return nouveau_arr

print (selectionSort([16, 2, 7, 4, 5,33]))