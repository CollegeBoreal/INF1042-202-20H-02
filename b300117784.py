# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 13:46:07 2020

@author: Bertrand
"""
# Functional Programming 

a=[x for x in range (0,10)]
print(a)
  
  # Impair 
s = [x for x in range(10) if x % 2 != 0]
 
print(s)

# Pair 
f = [x for x in range (10) if x % 2 == 0]
print(f)

#lambda

f = lambda x: x + 1
print f(2)




