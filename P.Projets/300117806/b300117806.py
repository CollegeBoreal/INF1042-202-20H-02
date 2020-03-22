# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 02:18:08 2020

@author: 
"""

#Tournoi entre 10 personnages de 3 classes diffÃ©rentes : guerrier, nain et mage

from random import randint

# ------------------------- classe personnage --------------------------
    
class Personnage:
    def __init__(self,nom,force,vie):
        self._nom = nom
        self._force_init = force        # points de force au dÃ©part
        self._vie_init = vie            # points de vie au dÃ©part
        self._force = force
        self._vie = vie
        self._victoires = 0             # nommbre de victoires
        
    def renaitre(self):
        self._force = self._force_init
        self._vie = self._vie_init
        
    def getNom(self) : return self._nom
    
    def getForce(self) : return self._force
    
    def getVie(self) : return self._vie
    
    def changeForce(self,combien) :
        self._force += combien
        
    def changeVie(self,combien) :
        self._vie += combien

    def getVictoires(self) : return self._victoires

    def incr_victoires(self) :
        self._victoires += 1
        
# --------------------------- classe guerrier ------------------------
    
class Guerrier(Personnage):
    def __init__(self,nom,force,vie):
        Personnage.__init__(self,nom,force,vie)
        
    def attaquer(self,qui):
        if self._force>0:
            qui.changeVie(-randint(0,self._force))
        
# ---------------------------- classe nain ---------------------------
    
class Nain(Personnage):
    def __init__(self,nom,force,vie):
        Personnage.__init__(self,nom,force,vie)
        
    def attaquer(self,qui):
        qui.changeVie(-2)
        if self._force>0:
            qui.changeForce(-randint(0,self._force))

# ---------------------------- classe mage ----------------------------

class Mage(Personnage):
    def __init__(self,nom,force,vie,mana):
        Personnage.__init__(self,nom,force,vie)
        self._mana_init = mana

    def renaitre(self):
        Personnage.renaitre(self)
        self._mana = self._mana_init
        
    def getMana(self) : return self._mana
    
    def attaquer(self,qui):
        if self._force>0:
            qui.changeVie(-randint(0,self._force)*self._mana)

    
# personnages
        
Merlin = Mage("Merlin",15,15,1)
Gandalf = Mage("Gandalf",10,10,2)
Saroumane= Mage("Saroumane",8,10,3)

Duroc = Guerrier("Duroc",15,15)
Nerosson = Guerrier("Nerosson",25,6)
GrosBill = Guerrier("Gros Bill",20,9)
Highlander = Guerrier("Highlander",9,30)

Gimli = Nain("Gimli",25,8)
Fridli = Nain("Fridli",8,12)
Heidi = Nain("Heidi",12,10)


# combats
# chaque combat a lieu deux fois pour Ã©viter une influence du 1er coup
def combattre(lui,moi):
    lui.renaitre()
    moi.renaitre()
    # print(lui.getNom(),"contre",moi.getNom(),end=" : ")
    while lui.getVie()>0 and moi.getVie()>0 :
        lui.attaquer(moi)
        if lui.getVie()<=0:
            # print(moi.getNom(), "a gagnÃ©")
            moi.incr_victoires()
        if moi.getVie()<=0:
            # print(lui.getNom(), "a gagnÃ©")
            lui.incr_victoires()
        if moi.getVie()>0 :
            moi.attaquer(lui)
            if lui.getVie()<=0:
                # print(moi.getNom(), "a gagnÃ©")
                moi.incr_victoires()
            if moi.getVie()<=0:
                # print(lui.getNom(), "a gagnÃ©")
                lui.incr_victoires()


# tournoi

concurrents=[Merlin, Gandalf, Saroumane, Duroc, Nerosson, GrosBill, Highlander, Gimli, Fridli, Heidi]
for i in range(500):
    for lui in concurrents:
        for moi in concurrents:
            if moi != lui:
                combattre(lui,moi)

# trier les rÃ©sultats

def swap(l,i,j):
    # echange 2 valeurs d'une liste
    t=l[i]
    l[i]=l[j]
    l[j]=t


for i in range(len(concurrents)-1):
    maxi=i
    for j in range(i+1,len(concurrents)):
        if concurrents[j].getVictoires()>concurrents[maxi].getVictoires(): maxi=j
    swap(concurrents,i,maxi)

# Ã©crire les rÃ©sultats
print()
print("RÃ©sultats")
print()
for lui in concurrents:
    print(lui.getNom(),":", lui.getVictoires(),"victoires")