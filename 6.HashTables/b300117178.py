# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:06:22 2020

@author: willfrid boris
"""

matiere={}
matiere["mathematique"]="brice robert"
matiere["reseau"]="richard"
print(matiere)


def ajout(book):
    a,c=book
    book=dict()
    book[a]=c
    return book

print( ajout(('tomate', 1.90)) )