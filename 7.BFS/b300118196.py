#-*- coding: utf-8 -*-
#winpty python 'nom du fichier python' notepzd readme.md
# breadth first search

from collections import deque

eleves = {}
eleves["Boris"]=["Amir","Franck","Nathalie","Bertrand"]
eleves["Amir"]=[]
eleves["Franck"]=[]
eleves["Nathalie"]=[]
eleves["Bertrand"]=["Erna","Hassana","Abdelkrim"]
eleves["Erna"]=[]
eleves["Hassana"]=[]
eleves["Zoureni"]=["Sekou","Auriane","Corlings"]
eleves["Sekou"]=[]
eleves["Auriane"]=[]
eleves["Corlings"]=[]
eleves["Abdelkrim"]=["Souleyman","Zack","Zoureni"]
eleves["Souleyman"]=[]
eleves["Zack"]=[]

def person_is_seller(name):
    return name == 'Zoureni'

    def search (name):
    search_queue = deque()
    search_queue +=eleves[name]
    while search_queue:
        person =search_queue.popleft()
        if person_is_seller(person):
            print (person + "", "have a mac")
            return True
        else:
            search_queue +=eleves[person]
    return False

search('Boris')
