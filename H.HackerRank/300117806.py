# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 12:32:28 2020

@author: User
"""


# how to write code selecion sort

def selectionsort(arr):
    
    #this value of i cprresponds to how many values were sorted
    
    for i in range (len(arr)):
        
        #we assume that the first item of the unsorted segment  is the smallest 
        
        lowest_value_index = i
        
        #this loop iterates over the unsorted items
        
        for j in range (i + 1, len(arr)):
            
            if arr[j] < arr[lowest_value_index]:
                
                lowest_value_index = j
                
                # swap value of the lowest unsorted element with the first unsorted element
                
                arr[j], arr[lowest_value_index], arr[i]
                
                #verify it works
                
                random_list_of_arr =[5, 8, 3, 20, 10, 1]
                
                selectionsort (random_list_of_arr)
                
                print (random_list_of_arr)