# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:23:03 2020

@author: playboikz
"""

eleves = {}
eleves ['Boris'] = ['Amir', 'Franck','Nathalie']
eleves ['Amir'] = []
eleves ['Franck'] = []
eleves['Nathalie'] = []


eleves['Bertrand'] = ['Erna','Hassana']
eleves['Erna']=[]
eleves['Hassna']=[]


eleves["Zoureni"]=["Sekou","Auriane","Corlings"]
eleves["Sekou"]=[]
eleves["Auriane"]=[]
eleves["Corlings"]=[]


eleves["Abdelkrim"]=["Souleyman","Zack"]
eleves["Souleyman"]=[]
eleves["Zack"]=[]


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
