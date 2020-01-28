# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:38:26 2020

@author: dell
"""

#how to write code selection sort


def selectionSort(arr) :

#this value of i corresponds to how many values were sorted
    
    for i in range (len(arr)):

# we assume that the first item of the unsorted segment is the smallest
        
        lowest_value_index = i
  
# this loop iterates over the unsorted items
        
        for j in range (i + 1, len(arr)) :
            
            if arr[j] < arr[lowest_value_index] :
                
                lowest_value_index = j
                
# swap values of the lowest unsorted element with the first unsorted element

        arr[i], arr[lowest_value_index] = arr[lowest_value_index], arr[i]                
        
 # verify it works
       
random_list_of_arr =[5, 8, 3, 20, 10, 1]

selectionSort (random_list_of_arr)

print (random_list_of_arr)