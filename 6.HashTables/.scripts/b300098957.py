# Mon code HashTable

robert = {}
robert['a'] = 1
robert['b'] = 2

etudiants = {}
etudiants[300116670] = 'Auriane'
etudiants[300117782] = 'Erna'

book = dict()
book['pomme'] = .99
book['avocat'] = 2.5
book['atieke'] = 5.0

def ajout(tuple):
   k, v = tuple
   book[k] = v
   return book

print(ajout(('ma_cle', [0,1,2,3,4])))