# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 13:22:27 2020

@author: fadde68
"""

eleves = {}
eleves["Boris"]=["Amir","Franck","Nathalie"]
eleves["Amir"]=[]
eleves["Franck"]=[]
eleves["Nathalie"]=[]
eleves["Bertrand"]=["Erna","Hassana"]
eleves["Erna"] = []
eleves["Hassana"] = []
eleves["Zouréni"] = ["Sekou", "Auriane", "Corlings"]
eleves["Sekou"] = []
eleves["Auriane"] = []
eleves["Corlings"] = []
eleves["Aldelkrim"] = ["Souleymane", "Zack"]
eleves["Souleymane"] = []
eleves["Zack"] = []

def personne_elue(name):
    return name == 'Zoureni'

from collections import deque

def search(name):
    visitees = []
    search_queue = deque()
    search_queue += eleves[name]
    while search_queue:
       personne = search_queue.popleft()
       if not personne in visitees:
          if personne_elue(personne):
             print(personne + " a le fameux Mac")
             return True
          search_queue += eleves[personne]
          visitees.append(personne)
    return False

if __name__== "__main__":
   search("Boris")




