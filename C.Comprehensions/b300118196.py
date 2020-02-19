# -*- coding : utf-8 -*-

# determinons les valeurs des différentes côtés d'un triangle rectangle
# telque la somme des cotés donne 24 et la valeur du plus grand côté donne 10

import math

def rightTriangle(max):
    x = [ (a, b, c)
    for c in range (11)
    for a in range (1,c+1)
    for b in range (1,a+1)
    

    if a**2 + b**2 == c**2 and a + b + c == 24]
    return(x)                   #retourner les valeurs obtenus
print(rightTriangle(24))        #
afficher le resultat obtenu de chaque côté dqns un tuple
