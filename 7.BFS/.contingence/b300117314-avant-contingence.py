
"""
Created on Sun Mar 22 17:05:52 2020

@author: Morti
"""

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



def personne_elue(name):

    return name == 'Zoureni'



from collections import deque



def search(name):

   search_queue = deque()

   search_queue += eleves[name]

   visitee = []

   while search_queue:

      personne = search_queue.popleft()

      if not personne in visitee:

         if personne_elue(personne):

            print(personne + " a le fameux Mac")

            return True

         else:

            search_queue += eleves[personne]

            visitee.append(personne)

   return False



search("Boris")
