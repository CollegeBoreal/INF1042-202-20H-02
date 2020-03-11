<<<<<<< HEAD
#Mon code HashTable Zack

robert = {}
robert ['a'] = 1
robert ['b'] = 2
print (robert)

print (robert ['b'])
etudiants = {}
etudiants [3001166782] = 'Aurianne'
etudiants [3001176700] = 'Erna'

print (etudiants)

book = dict()
book ['pomme'] = .99
book ['avocat'] = 2.5
book ['atieke'] = 5.0

print (book)
=======
#Mon code HashTable


recetteskabyles = {}
recetteskabyles ['hasbana'] = ['huile', 'tomtes', 'semoule', 'boeuf', 'razelhanout', 'menthe']
recetteskabyles ['brickaloeuf'] = ['feuilledebrick', 'oeufs', 'fromage', 'epices', 'huile']

def ajout(tuple):
    mousaoui, aitzetoun = tuple
    recetteskabyles [mousaoui] = aitzetoun
    return recetteskabyles

[ x for x in recetteskabyles.keys() ]
[ x for x in recetteskabyles.values() ]

print (ajout(('ma_cle',[0,1,2,3,4])))
>>>>>>> ad533b52ea0f6d310bf1965d86213703a02a1b17
