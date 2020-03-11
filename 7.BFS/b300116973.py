# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:07:14 2020

@author: dell
"""

#bfs

eleves ={}
eleves['boris'] = ['nathalie', 'franck','franck', 'amir']
eleves['amir']=[]
eleves["franck"]= []
eleves["nathalie"]=[]
eleves['bertrand']= ['erna', 'assana', 'boris']
eleves ['erna']=[]
eleves ["oriane"]=[]
eleves["souleumane"]=[]
eleves["zack"]=[]
eleves["abdelkrim"]=['zourenie','sekou']
eleves['assana']=[]
eleves["erna"]=[]
eleves["morteza"]=['idir','yassine']
eleves['idir']=[]
eleves["yassine"]=[]
eleves["zoureni"]=['nathalie','fofana']

def personne_speciale(name):
    return name == 'zoureni'

from collections import deque

def search(name) :
    search_queue = deque ()
    search_queue +=eleves [name]
    
    visitee = []

    while search_queue:
       personne=search_queue.popleft()
       if not personne in visitee:
          if personne_speciale:
             print(personne + " a le fameux mac")
             return True
          else:
             search_queue += eleves [personne]
    return False
search("abdelkrim")