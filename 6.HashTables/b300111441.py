# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 13:06:47 2020

@author: skofo
"""

concessionnaire = {}

concessionnaire ['voiture'] = ['toyota ','nissan','infinity','honda']
concessionnaire ['moto'] = ['cross','mate','zusuki','super yamaha']

def ajout(tuple):
    k, v  = tuple
    concessionnaire [k] = v 
    return concessionnaire
print(ajout(('ma_cle', [0,1,2,3,4])))
