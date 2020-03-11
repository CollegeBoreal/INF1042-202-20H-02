# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 14:50:27 2020

@author: Amir
"""
#creer un dictionnaire vide 
dictionnaire = {}
print (dictionnaire)


#injecter une element 
dictionnaire ["a"]= 1
print (dictionnaire)
# creons un dictionnaire avec les pays_touche_coronavirus
Pays_touche_coronavirus = {}

Pays_touche_coronavirus [1] = 'China'
Pays_touche_coronavirus [2] = 'Japan'
Pays_touche_coronavirus [3] =  'Etats-Uns'
Pays_touche_coronavirus [4] =  ' Royaume-Unis '

print (Pays_touche_coronavirus)

Temp = ('minute',60)

c,d = Temp
print (Temp)

# creons une fonction 
def ajout (tuple) :
     a,b = tuple
     Pays_touche_coronavirus [a] = b
     return Pays_touche_coronavirus
 
print (ajout(('ma_cle', [0,1,2,3,4])))
