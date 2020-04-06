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

def main():
  print('Informatique: le rêve')

def personne_elue(name):
    return name == 'Corlings'

from collections import deque

def search(name):
    visitees = []
    search_queue = deque()
    search_queue += eleves[name]
    while search_queue:
       personne = search_queue.popleft()
       if not personne in visitees:
          if personne_elue(personne):
             print(personne + " est personne elue")
             return True
          search_queue += eleves[personne]
          visitees.append(personne)
    return False

if __name__== "__main__":
   search("Boris")
