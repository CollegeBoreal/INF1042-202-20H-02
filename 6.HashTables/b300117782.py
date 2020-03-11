# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 11:16:38 2020

@author: User
"""

culture = {}

culture['Africaine'] = ['bamileke', 'eyondo','bassa','toupouri']

culture['Europenne'] = ['art','musique','litterature','architecture']

print(culture)

def ajout(tuple):
    x,y = tuple
       
    culture [x] = y
       # rajouter de tuple
       
    return culture

print (ajout(('ma_cle',[0,1,2,3,4])))