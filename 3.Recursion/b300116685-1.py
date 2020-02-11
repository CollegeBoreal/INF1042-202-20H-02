# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:13:54 2020

@author: Amir
"""

def binary_search(num_list) :
    if len (num_list) ==1 :
        return num_list [0]
    else:
        return  num_list [0]+ binary_search(num_list[1:])

print(binary_search([2,4,5,6,7])) 