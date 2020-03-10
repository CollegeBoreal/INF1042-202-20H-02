# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:14:36 2020

@author: kdmar
"""
film = {}

film["action"] = ["Fast and Furious ","24h chrono","Lucie","Jumanji"]

film["comedie"] = ["Think like a man","Death at funerals","Ride along","Bad boys for life"]

film["thriller"] = ["IT","Black Christmas","MA","Get out" ]



def ajout(tuple):
    a,m = tuple
    film[a] = m
    return film

print(ajout(("ma_cle",[0,1,2,3,4])))

    
    

