# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:05:56 2020

@author: dell
"""

robert = {}
robert ["a"] = 1
print (robert)

robert ['b'] = 2

print (robert)
etudiants = {}
etudiants [300116673] = "nathalie"
etudiants [300116670] = "auriane"
etudiants [300117782] = "erna"
print (etudiants)
t = ('a', 5.0)
a, b = t
print (t)


recette = {}
recette ["mafe"] = ['huile', 'eau', 'poisson', 'epices', 'tomates']
recette ['canadienne']=['maple', 'spaguetti', 'champignons', 'pizza']

print(recette)

def ajout (tuple):
    x,y =tuple
    
    recette [x] = y
    
    return recette

print (ajout(('ma_cle', [0,1,2,3,4])))









