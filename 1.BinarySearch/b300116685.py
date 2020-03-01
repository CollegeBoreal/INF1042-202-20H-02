# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 18:13:34 2020

@author: Amir
"""
def binary_search (list, item) :
    low = 0
    high = len (list) -1
   
    while low <= high :
        
        mid = (low + high)//2
        guess = list[mid]
        
        if guess == item :
            return mid
        
        if guess > item :
            high = mid -1
        
        else :
            low = mid + 1
            

<<<<<<< HEAD
def binary_search (list, item) :
    low = 0
    high = len (list) -1
   
    while low <= high :
        
        mid = (low + high)//2
        guess = list[mid]
        
        if guess == item :
            return mid
        
        if guess > item :
            high = mid -1
        
        else :
            low = mid + 1
            
=======
    return None

my_list = [5, 7, 7, 11, 14, 19, 20, 25]



print (binary_search (my_list, 25))
print (binary_search (my_list, 14))
>>>>>>> e1c2bbe03e8b7a3161aecaf721eb449ac36411fc

    return None

my_list = [5, 7, 7, 11, 14, 19, 20, 25]



<<<<<<< HEAD
print (binary_search (my_list, 25))
print (binary_search (my_list, 14))
=======
>>>>>>> e1c2bbe03e8b7a3161aecaf721eb449ac36411fc
