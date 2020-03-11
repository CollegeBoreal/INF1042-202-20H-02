# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 15:13:09 2020

@author: Bertrand
"""

Musiques = {}

Musiques['Africaine'] = ['Makossa', 'Ndombolo','Coupedecale','Bensikin']

Musiques['Europenne'] = ['Jazz','classique','Versaille','Salsa']

print(Musiques)

def ajout(tuple):
    k,v = tuple
       
    Musiques [k] = v
       # rajouter le tuple
       
    return Musiques

print (ajout(('ma_cle',[0,1,2,3,4])))