
# -*- coding: utf-8 -*-

"""
Created on Tue Mar 10 15:07:27 2020

@author: zacks
Créer un dictionnaire étudiant 

"""
eleves = {}
eleves ['Boris'] = ['Amir', 'Franck','Nathalie','Bertrand']
eleves ['Amir'] = []
eleves ['Franck'] = []
eleves['Nathalie'] = []
eleves['Bertrand'] = ['Erna','Hassana','Abdelkrim']
eleves["Erna"]=[]
eleves["Hassana"]=[]
eleves["Zoureni"]=["Sekou","Auriane","Corlings"]
eleves["Sekou"]=[]
eleves["Auriane"]=[]
eleves["Corlings"]=[]
eleves["Abdelkrim"]=["Souleyman","Zack","Zuremi"]
eleves["Souleyman"]=[]
eleves["Zack"]=[]

def personne_elue(name):
    return name == 'Zureni'
from collections import deque
    
def search (name):
    search_queue = deque()
    search_queue += eleves [name]
    searched = []
    while search_queue:
         personne = search_queue.popleft()
         if not personne in searched:
           if personne_elue (personne):
            print (personne + "a le fameux Mac")
            return True
    else:
        search_queue += eleves [personne]
        searched.append (personne) 
    return False

search  ("Boris")

        
    
    
    
    
    
    