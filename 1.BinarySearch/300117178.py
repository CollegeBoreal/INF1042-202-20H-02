# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:04:41 2020

@author: willfrid boris
"""
def binary_seach(list,item):
    low=0
    hight=len(my_list)-1
    
    while low <=hight:
        mid=(low+hight)//2
        guess=list[mid]
        if(guess==item):
            return mid
        if(guess > item):
            hight= mid-1
        else:
            low=mid+1
    return None
my_list=[5,7,11,14,19,20,25]
print(binary_seach(my_list,11))
