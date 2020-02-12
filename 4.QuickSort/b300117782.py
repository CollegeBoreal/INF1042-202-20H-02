# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:19:34 2020

@author: User
"""

def quicksort ( array ):
    # base case
    
    if len ( array ) < 2:
        return array
    else:
       #recursive case
       
        pivot = array [ 0 ]
        
        less = [ i for i in array [ 1: ] if i <= pivot]
        
        greater = [ i for i in array [ 1:] if i > pivot]
        
        return quicksort ( less ) + [ pivot] + quicksort( greater )
    
print( quicksort ([ 10, 270, 30, 40, 2, 60, 13, 4, 3, 0 ]))