# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 11:16:28 2020

@author: Idir

COMMENTAIRE 

"""

def TrouvPlusPetit(arr):
    
        LaPlusPetite = arr[0]
        LaPlusPetite_index = 0
        
        for i in range(1, len(arr)):
            if arr[i] < LaPlusPetite:
                LaPlusPetite = arr[i]
                LaPlusPetite_index = i
        
        return LaPlusPetite_index


def selectionSort(arr):
 
    newArr = []
 
    for i in range(len(arr)):
      smallest = TrouvPlusPetit(arr)
      newArr.append(arr.pop(smallest ))
 
    return newArr
print (selectionSort([38, 2, 10, 74, 45, 12, 99, 7])) # AFFICHER LES CHIFFRES EN ORDRES 
