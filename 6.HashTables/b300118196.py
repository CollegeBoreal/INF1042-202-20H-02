# -*- coding: utf-8 -*-

robert = {}

robert["a"]= 1
robert["b"]= 2

print(robert)


""" programme qui retourne un dictionnaire comprenant la cle et la valeur
fournit par le tuple print(ajout("ma_clé", [0,1,2,3,4])) """

def ajout(tuple):

    book = {"fables de la montagne": "tale","give and take": "motivation book","opera": "tale", \
            "la vie est belle": "parodie","la joconde": "art","le grand palais": "art and culture"}
    return book
print(ajout(3))
