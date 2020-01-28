#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 18:21:31 2020

@author: zoureni
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

print (selectionSort([12, 2, 23, 72, 8,33]))
