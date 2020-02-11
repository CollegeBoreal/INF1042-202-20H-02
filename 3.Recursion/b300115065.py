"""
Created on Tue Feb  4 15:37:34 2020

@author: akram fadde
"""

def fact(x):
    if x==1:
        return 1
    else:
        return (x*fact(x-1))

print (fact(45))
