# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 12:35:28 2020

@author: Lenovo G20
"""

Hassana = {}
Hassana['a'] = 1 
Hassana['b'] = 2
print(Hassana['a'])
print(Hassana['b'])


etudiants = {}
etudiants[300117806] = 'Hassana'
etudiants[300117890]= 'lambda'
print(etudiants)


book = dict()
book['salade'] = 2.95
book['concombre'] = 1.75
book['mayonnaise']=1.05
print(book)


def ajout(tuple):
    k,v = tuple
    book[k] = v
    return book

print(ajout(('ma_cle', [0,1,2,3,4])))