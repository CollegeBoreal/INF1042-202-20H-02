""
Created on Wed Jan 09 14:01:02 2020

@author: idir

LayLayLay

"""


def recherche_binaire(list,article):
    ValeurMini = 0
    ValeurMaxi = len(ma_liste)-1
    
    
    while ValeurMini <= ValeurMaxi:
        mid= (ValeurMini + ValeurMaxi)//2
        guess = list[mid]
        if guess == article :
           return mid
        if guess > article:
           ValeurMaxi = mid - 1
        else:
            ValeurMini = mid + 1
    return None 



ma_liste = [1,7,11,14,19,20,25]


print (recherche_binaire(ma_liste, 7))
print (recherche_binaire(ma_liste, 20))
print (recherche_binaire(ma_liste, 21))
