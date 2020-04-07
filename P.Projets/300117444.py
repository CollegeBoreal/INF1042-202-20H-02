# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 13:12:35 2020

@author: idira
"""
def add():
    print ('Vous avez choisi l\'addition ! Parfait, commençons.')
    chfUN=input('Entrez un nombre : ')
    chfUN=eval(chfUN)

    chfSE=input('Entrez un second nombre : ')
    chfSE=eval(chfSE)

    resultat = chfUN + chfSE
    print ('Donc, %s + %s est égal à %s !'%(chfUN,chfSE,resultat))

    res=input('Voulez-vous recommencez ? Y/N ')
    res = res.upper()

    if res == 'Y':
        print ('\n \n')
        choix()
    elif res == 'N':
        print ('Bye !')
    else:
        print('Je t\'avais demandé Y ou N !!!')

def sous():
    print ('Vous avez choisi la soustraction ! Parfait, commençons.')
    chfUN=input('Entrez un nombre : ')
    chfUN=eval(chfUN)

    chfSE=input('Entrez un second nombre : ')
    chfSE=eval(chfSE)

    resultat = chfUN - chfSE

    print ('Donc, %s - %s est égal à %s !'%(chfUN,chfSE,resultat))

    res=input('Voulez-vous recommencez ? Y/N ')
    res = res.upper()

    if res == 'Y':
        print ('\n \n')
        choix()
    elif res == 'N':
        print ('Bye !')
    else:
        print('Je t\'avais demandé Y ou N !!!')

def multi():
    print ('Vous avez choisi la multiplication ! Parfait, commençons.')
    chfUN=input('Entrez un nombre : ')
    chfUN=eval(chfUN)

    chfSE=input('Entrez un second nombre : ')
    chfSE=eval(chfSE)

    resultat = chfUN * chfSE

    print ('Donc, %s x %s est égal à %s !'%(chfUN,chfSE,resultat))

    res=input('Voulez-vous recommencez ? Y/N ')
    res = res.upper()

    if res == 'Y':
        print ('\n \n')
        choix()
    elif res == 'N':
        print ('Bye !')
    else:
        print('Je t\'avais demandé Y ou N !!!')

def div():
    print ('Vous avez choisi la division ! Parfait, commençons.')
    chfUN=input('Entrez un nombre : ')
    chfUN=eval(chfUN)

    chfSE=input('Entrez un second nombre : ')
    chfSE=eval(chfSE)

    resultat = chfUN / chfSE

    print ('Donc, %s : %s est égal à %s !'%(chfUN,chfSE,resultat))

    res=input('Voulez-vous recommencez ? Y/N ')
    res = res.upper()

    if res == 'Y':
        print ('\n \n')
        choix()
    elif res == 'N':
        print ('Bye !')
    else:
        print('Je t\'avais demandé Y ou N !!!')

def choix():
    type=input('Entrez le type d\'opération que vous voulez faire (Addition, soustraction, division ou multiplication) : ')
    type = type.lower()

    if type == 'addition':
        add()
    elif type =='soustraction':
        sous()
    elif type =='multiplication':
        multi()
    elif type == 'division':
        div()
    else:
        print('Tu n\'as pas répondu à ma question !!!')
        choix()
    
choix()
