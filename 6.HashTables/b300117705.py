# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 15:26:20 2020

@author: acorl
"""

Series = {}

Series['Policier'] = ['FBI', '24 Chrono','The Mentalist','NCIS']

Series['Fictions'] = ['ARROW','Flash','Super Girl','Black Mirror']

print(Series)

def ajout(tuple):
    k,v = tuple
       
    Series [k] = v
      
       
    return Series

print (ajout(('ma_cle',[0,1,2,3,4])))