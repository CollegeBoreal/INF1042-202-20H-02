
"""
Created on Wed Mar  4 14:23:29 2020

@author: akram fadde
"""

Maroc= {}
Maroc['a']= 12
print(Maroc)
Maroc['b']= 20
print(Maroc)

Maroc['c']= 3
print(Maroc['c'])


Mon_pays={}

Mon_pays[1]= 'casablanca'
print(Mon_pays)
Mon_pays [2]='RABAT'
print(Mon_pays)
Mon_pays[3]='TANJA'
print(Mon_pays)
Mon_pays[4]='Jadida'
print("jaime Mon_pays:", Mon_pays)


def ajout (tuple) :
     a,b = tuple
     Mon_pays[a] = b
     return Mon_pays
 
print (ajout(('ma_cle', [0,1,2,3,4])))


