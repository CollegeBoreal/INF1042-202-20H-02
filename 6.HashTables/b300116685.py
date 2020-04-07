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
# creons un dictionnaire avec les pays africains
Pays_Africain = {}

Pays_Africain [1] = 'Djibouti'
Pays_Africain [2] = 'Somalie'
Pays_Africain [3] =  'Cameroun'
Pays_Africain [4] =  ' Kenya '

print (Pays_Africain)

Temp = ('minute',60)

c,d = Temp
print (c,d)
print (Temp)

# creons une fonction 
def ajout (tuple) :
     a,b = tuple
     Pays_Africain [a] = b
     return Pays_Africain
 
print (ajout(('ma_cle', [0,1,2,3,4])))
