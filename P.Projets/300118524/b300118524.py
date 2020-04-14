#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:31:36 2020

@author: zoureni
"""


#importation du module aléatoire
import random

#création de la liste des mots que comporte le jeu
dictionnaire_du_jeu = ["jeu", "mot"]

#importation du module horaire
import time

#accueillir l'utilisateur
joueur = input(str("Quel est votre nom? "))

print ("SALUT, " + joueur, "Il est temps de jouer au jeu du pendu !")

#temps d'attente de 3 secondes
time.sleep(2)

print ("COMMENÇONS...")
time.sleep(2)

#le mot à trouver est choisi de manière aléatoire
mot_a_trouvé = random.choice(dictionnaire_du_jeu)

#crée une variable avec une valeur vide
mot_déviné = ''

#déterminer le nombre de tours à partir de la longueur du mot à trouvé
tours = len(mot_a_trouvé)
print("Vous avez",len(mot_a_trouvé)," essai pour trouver le mot")

# Créer une boucle while
#vérifier si les tours sont supérieures à zéro
while tours > 0:         

    # faire un compteur qui commence par zéro
    echec = 0             

    # pour chaque caractàre dans le mot à trouver  
    for char in mot_a_trouvé:      

    # voir si le caractàre est dans le mot deviné par le joueur
        if char in mot_déviné:    
    
        # imprimer puis sortir le caractàre
            print (char,)    

        else:
    
        # s'il n'est pas trouvé, imprimer un tiret
            print ("_",)     
       
        #augmenter le compteur échec avec un
            echec += 1    

    # si échec est égal à zéro
    # imprimer "Félicitations"
    if echec == 0:        
        print ("Félicitations ") 

    #quitter le script
        break              

    print

    # demander à l'utilisateur de deviner un caractère
    caractere_devine = input(str("Déviner une lettre:"))
       

    #faire deviner aux joueurs en prenant juste la première lettre
    mot_déviné += caractere_devine[0]                    

    # si la supposition ne se trouve pas dans le mot à trouvé
    if caractere_devine not in mot_a_trouvé:  
 
     #le compteur de tours diminue de 1
        tours -= 1        
 
    # imprimer erreur
        print ("la lettre  " + caractere_devine[0], "ne fait pas partie du mot à déviné")    
 
    # le nombre de tours qui reste
        print ("Vous avez encore ", + tours, 'essai ') 
 
    # si les tours sont égaux à zéro
        if tours == 0:           
    
        # imprimer "Vous avez perdu"
            print ("Vous avez perdu")
            print ("le mot secret est ..." + mot_a_trouvé, "...")