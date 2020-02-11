# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:53:18 2020

@author: Bertrand
"""

# BinarySearch 


def binary_search(list, item):
    low = 0
    high = len(list)-1
    
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
            


my_list =[5, 7, 11, 14, 19, 20, 25]


print(binary_search(my_list, 25))
print(binary_search(my_list, -1))
