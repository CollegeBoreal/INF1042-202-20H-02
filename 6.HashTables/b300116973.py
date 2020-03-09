# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:05:56 2020

@author: dell
"""

livre = {}

livre['classique'] = ['moumbutu', 'jean de dieu momo','mamadou et binera','mon ecole']

livre['fiction'] = ['commando','brussle','24heurechrono','matrice']

print(livre)

def ajout(tuple):
    l,m = tuple
       
    livre [l] = m
       # rajouter le tuple
       
    return livre

print (ajout(('ma_cle',[0,1,2,3,4])))












