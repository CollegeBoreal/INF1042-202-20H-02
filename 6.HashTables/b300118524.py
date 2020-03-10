#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:09:07 2020

@author: zoureni
"""

zoureni = {}
zoureni['a'] = 1
zoureni['b'] = 2
print(zoureni['a'])
print(zoureni['b'])

etudiants = {}
etudiants[300118524] = 'zouréni'
etudiants[300110000] = 'lambda'
print(etudiants)

book = dict()
book['pomme'] = .99
book['avocat'] = 2.5
book['atieke'] = 5.0
print(book)

ordinateur ={}
ordinateur ['primaire']= ['processeur', 'mémoire RAM', 'boite alimentation']
ordinateur['secondaire'] = ['lecteur optique', 'carte son', 'carte graphique']







def ajout(tuple):
   k, v = tuple
   ordinateur[k] = v
   return ordinateur
 


print (ajout(('ma_cle',[0,1,2,3,4])))

