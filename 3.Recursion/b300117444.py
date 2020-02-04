# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:25:53 2020

@author:Idir .
"""

print("******************BIENVENUE********************")
print("***********************************************")
a=int(input("entrer un chiffre\n") )
x =a
def fact(x):
    if(x==1):
        return 1
    else:
        return x*fact(x-1)
print("Le resultat est :")
print(fact(x))
