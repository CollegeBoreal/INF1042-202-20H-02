#calcul de fonction factorielle

def fact(x):
    
    #si x est egal a 1 retourne sinon continu le calcul et affiche resultat
    if(x==1):
        
        return 1
    
    else:
        
        return x*fact(x-1)
    
    # afficher le resultat final

print(fact(5))
